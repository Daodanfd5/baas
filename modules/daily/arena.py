import time

from common import ocr, color, stage, image
from modules.baas import home

x = {
    'id': (476, 424, 496, 442),
    'cd': (153, 516, 212, 535),
    '0-5': (194, 479, 227, 497),
    'skip': (1109, 591, 1135, 614)
}
render = {
    'config.less_level': {
        "type": "num",
        "name": "攻击低我N级",
        "desc": "只会找低于我N级的对手，如果实在找不到会降低等级继续寻找",
        "opts": {
            "min": "0",
            "max": "50",
            "step": "1"
        }
    },
    'config.max_refresh': {
        "type": "num",
        "name": "每轮刷新次数",
        "desc": "如果找不到对手，会降低地方1级条件继续刷新，直到找到满足条件的对手为止",
        "opts": {
            "min": "1",
            "max": "50",
            "step": "1"
        }
    }
}
finish_seconds = 55


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus')

    # 点击战术对抗赛
    self.click(1093, 524)
    # 等待加载
    ocr.screenshot_check_text(self, '战术对抗赛', (102, 6, 248, 41))

    # 开始战斗
    start_fight(self)

    # 回到首页
    home.go_home(self)


def get_prize(self):
    if color.check_rgb_similar(self, (320, 400, 321, 401)):
        # 领取时间奖励
        self.click(353, 385)
        # 关闭奖励
        stage.close_prize_info(self)
    if color.check_rgb_similar(self, (330, 480, 331, 481)):
        # 领取挑战奖励
        self.click(348, 465)
        # 关闭奖励
        stage.close_prize_info(self)


def start_fight(self, wait=False):
    # 检查余票
    time.sleep(0.5)
    if image.compare_image(self, 'arena_0-5', 0):
        self.logger.info("没票了")
        get_prize(self)
        return True
    # 检测已有冷却
    if wait or not image.compare_image(self, 'arena_cd', 0):
        self.finish_seconds = finish_seconds
        return False
    # 选择对手
    choose_enemy(self)
    # 编队
    self.click(640, 570, True, 1, 0.5)
    # 等待出击加载
    ocr.screenshot_check_text(self, '出击', (1134, 650, 1207, 683))

    # 检查跳过是否勾选
    image.compare_image(self, 'arena_skip', 999, 20, False, self.click, (1125, 599, False), 0.5)

    # 角色加载太慢了... 暂时没有好办法 todo 吧
    time.sleep(3)
    # 出击
    self.double_click(1175, 665, True, 1, 1)
    while True:
        # 检查有没有出现ID
        if image.compare_image(self, 'arena_id', 0):
            break
        # 关闭弹窗
        self.click(1235, 82, False)
        time.sleep(self.bc['baas']['ss_rate'])
    start_fight(self, True)


def choose_enemy(self):
    less_level = int(self.tc['config']['less_level'])
    # 识别自己等级
    my_lv = float(ocr.screenshot_get_text(self, (165, 215, 208, 250), self.ocrNum))
    refresh = 0
    while True:
        # 超出最大次数,敌人预期等级-1
        if refresh > self.tc['config']['max_refresh']:
            less_level -= 1
            refresh = 0
            continue
        # 识别对手等级
        enemy_lv = float(ocr.screenshot_get_text(self, (551, 298, 581, 317), self.ocrNum))
        self.logger.info("对手等级 {0}".format(enemy_lv))
        if enemy_lv + less_level <= my_lv:
            break
        # 更换对手
        self.double_click(1158, 145)
        refresh += 1
    # 选择对手
    self.click(769, 251)
