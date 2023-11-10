from common import image, stage
from modules.baas import home

x = {
    'notice': (589, 151, 619, 182),
    'notice2': (588, 167, 619, 197),
    'limited': (610, 146, 640, 175),  # 购买次数上限 或 持有体力上限
    'buy20': (632, 268, 656, 288),
    'buy19': (632, 268, 656, 288),
    'buy18': (632, 268, 656, 288),
    'buy17': (632, 268, 656, 288),
    'buy16': (632, 268, 656, 288),
    'buy15': (632, 268, 656, 288),
    'buy14': (632, 268, 656, 288),
    'buy13': (632, 268, 656, 288),
    'buy12': (632, 268, 656, 288),
    'buy11': (632, 268, 656, 288),
    'buy10': (632, 268, 656, 288),
    'buy9': (632, 268, 656, 288),
    'buy8': (632, 268, 656, 288),
    'buy7': (632, 268, 656, 288),
    'buy6': (632, 268, 656, 288),
    'buy5': (632, 268, 656, 288),
    'buy4': (632, 268, 656, 288),
    'buy3': (632, 268, 656, 288),
    'buy2': (632, 268, 656, 288),
    'buy1': (632, 268, 656, 288),
}


def start(self):
    # 回到首页
    home.go_home(self)

    # 点击购买体力
    self.d.double_click(619, 37)

    # 购买上限检查
    if image.compare_image(self, 'buy_ap_limited', 5):
        return home.go_home(self)

    # 等待购买AP弹窗加载
    image.compare_image(self, 'buy_ap_notice')

    try:
        need_count = self.tc['config']['count']
        purchased_count = 20 - calc_surplus_count(self)
        # 次数已满
        if need_count <= purchased_count:
            return home.go_home(self)
        # 计算还要购买的次数
        buy_count = need_count - purchased_count
        # 增加次数
        self.click(806, 345, False, buy_count - 1)
        # 点击确认
        self.d.click(770, 501)

        # 确认购买弹窗检测
        if image.compare_image(self, 'buy_ap_notice2', 5):
            # 再次确认购买
            self.d.click(768, 485)

        # 确认超出持有上限弹窗
        if image.compare_image(self, 'buy_ap_limited', 5):
            # 查找和购买体力相关任务，重新运行
            exec_next_task(self)
            # 自己也重新运行
            self.finish_seconds = 30
            return home.go_home(self)

        # 关闭获得奖励
        stage.close_prize_info(self, False, True)
        # 查找和购买体力相关任务，重新运行
        exec_next_task(self)
        # 如果要购买的次数大于3次,1分钟后重新运行该任务
        if buy_count > 3:
            self.finish_seconds = 30
    except ValueError:
        print("次数识别失败")
    home.go_home(self)


def calc_surplus_count(self):
    """
    计算剩余购买次数,这里必须用图片匹配才能精准,用文字识别小数字必出bug
    """
    for i in range(20, 0, -1):
        if image.compare_image(self, 'buy_ap_buy{0}'.format(i), 5):
            return i
    return 0


def exec_next_task(self):
    """
    立刻执行和购买ap相关的任务
    """
    if self.tc['config']['exec'] == '':
        return
    self.finish_seconds = 1
    self.finish_task(self.tc['config']['exec'])
    self.finish_seconds = 0
