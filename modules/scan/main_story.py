import time

from common import color, stage, image
from modules.baas import home

x = {
    'story': (107, 9, 162, 36),
    'menu': (107, 9, 162, 36),
    'choose-plot': (107, 9, 162, 36),
    'clearance': (861, 188, 983, 205),
    'current-clearance': (855, 188, 1010, 205),
    'first-lock': (1102, 225, 1131, 257),
    'plot-info': (577, 145, 640, 174),
    'plot-fight': (901, 211, 925, 236),
    'plot-attack': (107, 9, 162, 36),  # 部队出击
    'fight-parse': (1223, 32, 1243, 59),  # 战斗中暂停按钮
    'fight-confirm': (1144, 649, 1194, 674)  # 战斗结果

}
render = {
    "base": {
        "name": "功能设置"
    },
}

story_position = {
    1: (350, 345), 2: (950, 345)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus', mis_fu=self.click, mis_argv=(1195, 576))

    # 点击故事
    self.click(1093, 273)
    image.compare_image(self, 'main_story_story')

    # 点击主线故事
    self.click(248, 355)
    image.compare_image(self, 'main_story_menu')

    # 选择故事
    select_story(self)

    # 开始剧情
    start_admission(self)

    # 回到首页
    home.go_home(self)


def skip_polt(self):
    """
    跳过剧情
    @param self:
    @return:
    """
    while True:
        # 等待菜单出现
        image.compare_image(self, 'cm_skip-menu')
        # 点击菜单
        self.click(1204, 40, False)
        # 点击>>
        self.click(1210, 120, False, 1, 1)
        # 等待跳过加载
        if image.compare_image(self, 'cm_confirm', 3):
            # 点击跳过
            self.click(770, 521, False)
            return


def start_admission(self):
    # 检查是否通关
    if image.compare_image(self, 'main_story_clearance', 0, 10):
        return
    # 检查是否通关
    if image.compare_image(self, 'main_story_current-clearance', 0, 10):
        return
    # 查看第一个是否锁住了
    if image.compare_image(self, 'main_story_first-lock', 10, 20):
        # 锁住了点第二个任务
        self.click(1114, 339, False)
    else:
        self.click(1114, 237, False)
    # 等待剧情信息加载
    image.compare_image(self, 'main_story_plot-info')

    is_fight = image.compare_image(self, 'main_story_plot-fight', 0, 10)

    # 进入剧情
    self.click(641, 516, False)
    # 跳过剧情
    skip_polt(self)

    if is_fight:
        # 等待部队出击页面加载
        image.compare_image(self, 'main_story_plot-attack')
        time.sleep(3)
        # 点击出击
        self.click(1158, 655, False)
        auto_fight(self)
        # 跳过剧情
        skip_polt(self)

    # 关闭获得奖励
    stage.close_prize_info(self)
    time.sleep(2)
    # 再次递归
    return start_admission(self)


def auto_fight(self):
    # 等待战斗加载
    image.compare_image(self, 'main_story_fight-parse', need_loading=True)
    # 3倍减速检测
    if not color.check_rgb_similar(self, (1177, 614, 1178, 615), (39, 231, 255)):
        self.click(1208, 623, False)
        time.sleep(0.5)
    # 3倍减速检测
    if not color.check_rgb_similar(self, (1177, 614, 1178, 615), (39, 231, 255)):
        self.click(1208, 623, False)
        time.sleep(0.5)
    # 点击自动
    if not color.check_rgb_similar(self, (1169, 664, 1170, 665), (39, 231, 255)):
        self.click(1208, 673, False)
    time.sleep(10)
    # 等待战斗结束
    image.compare_image(self, 'main_story_fight-confirm')
    # 确认战斗结果
    time.sleep(1)
    self.double_click(1168, 659)


def select_story(self):
    """
    选择故事
    @param self:
    @return:
    """
    story = self.tc['config']['story']
    quotient = (story - 1) // 2
    self.click(1246, 335, False, quotient, 0.5)
    zb = 1 if story % 2 == 1 else 2
    image.compare_image(self, 'main_story_choose-plot', mis_fu=self.click, mis_argv=(*story_position[zb], False))
