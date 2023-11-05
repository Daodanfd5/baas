import time

from modules import home
from utils import ocr

entrust_position = {
    'jdfy': (962, 270), 'xyhs': (962, 410)
}

level_position = {
    1: (1116, 185), 2: (1116, 285), 3: (1116, 385), 4: (1116, 485),
    5: (1116, 330), 6: (1116, 430), 7: (1116, 530), 8: (1116, 630),
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    ocr.is_business(self)

    # 点击特别委托
    self.click(727, 570)
    # 选择委托
    choose_entrust(self, entrust_position)
    # 回到首页
    home.go_home(self)


def choose_entrust(self, position):
    for tk in self.tc['config']:
        # 等待加载
        wait_loading_entrust(self)
        # 选择委托
        self.click(*position[tk['entrust']])
        # 等待加载
        ocr.screenshot_check_text(self, '关卡列表', (889, 99, 979, 125))

        part1_swipe = False
        part2_swipe = False

        if tk['stage'] <= 4 and not part1_swipe:
            part1_swipe = True
            self.d.swipe(933, 230, 933, 586)
            time.sleep(0.5)
        if tk['stage'] >= 5 and not part2_swipe:
            part2_swipe = True
            self.d.swipe(933, 586, 933, 230)
            time.sleep(0.5)
        # 点击关卡
        self.click(*level_position[tk['stage']])
        # 等关卡加载
        ocr.screenshot_check_text(self, '任务信息', (574, 122, 709, 155))
        # 扫荡指定次数
        self.click(1034, 299, False, tk['count'] - 1, 0.6)
        # 点击开始扫荡
        self.d.click(938, 403)
        if self.tc['task'] == 'special_entrust':
            # 查看体力是否足够
            if ocr.screenshot_check_text(self, '是否购买', (515, 227, 627, 260), 0, 0.5):
                # 关闭弹窗 返回首页
                home.go_home(self)
                return
        else:
            # 查看入场券是否足够
            if ocr.screenshot_check_text(self, '移动', (730, 485, 803, 516), 0, 0.5):
                # 下一个
                self.click(56, 38, 0, 3)
                continue
        # 等待确认加载
        ocr.screenshot_check_text(self, '通知', (599, 144, 675, 178))
        # 确认扫荡
        self.d.click(770, 500)
        # 检查跳过,最多检查30次
        if tk['count'] >= 3:
            ocr.screenshot_check_text(self, '跳过', (600, 488, 684, 526), 30)
            # 点击跳过
            self.d.click(641, 504)
        # 等待结算
        ocr.screenshot_check_text(self, '确认', (597, 562, 680, 600))
        # 确认奖励
        self.d.click(641, 580)
        # 返回委托
        back_entrust(self)


def back_entrust(self):
    # 查看是否有任务信息弹窗
    if not ocr.screenshot_check_text(self, '任务信息', (574, 122, 709, 155), 5, 0.5):
        return
    self.click(56, 38, 0, 2, 1)


def wait_loading_entrust(self):
    # 等待加载
    if self.tc['task'] == 'special_entrust':
        ocr.screenshot_check_text(self, '信用回收', (1044, 362, 1222, 414))
    else:
        ocr.screenshot_check_text(self, '讲堂', (1126, 506, 1222, 557))
