import sys
import time

from common import ocr, color, stage, image
from modules.baas import home, cm
from modules.scan import hard_task, main_story

x = {
}

normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}
force_position = {
    1: (124, 195), 2: (124, 277), 3: (124, 354), 4: (124, 429),
}
stage_data = {
    '14-1': {
        'start': {
            '1': (460, 383),  # 1队开始坐标
            '2': (572, 303)  # 2队开始坐标
        },
        'attr': {
            '1': 'burst1',  # 1队爆发
            '2': 'mystic1'  # 2对神秘
        },
        'action': [
            # 神秘➡️ 爆发↘️
            {'t': 'click', 'p': (756, 388), 'ec': True}, {'t': 'click', 'p': (636, 555), 'ec': True, 'wait': 10},
            # 神秘➡️ 爆发↘️
            {'t': 'click', 'p': (867, 316), 'ec': True}, {'t': 'click', 'p': (619, 461), 'ec': True, 'wait': 5},
            # 神秘➡️ 爆发↘️
            {'t': 'click', 'p': (839, 298), 'ec': True}, {'t': 'click', 'p': (669, 491), 'ec': False},
        ]
    },
    '14-2': {
        'start': {
            '1': (611, 299),  # 1队开始做坐标
            '2': (880, 559)  # 2对开始坐标
        },
        'attr': {
            '1': 'burst1',  # 1队爆发
            '2': 'mystic1'  # 2对神秘
        },
        'action': [
            # 神秘↖️  爆发↘️
            {'t': 'click', 'p': (691, 385), 'ec': True}, {'t': 'click', 'p': (590, 393), 'ec': True},
            # 切换到爆发
            {'t': 'exchange', 'ec': True},
            # 爆发↙️  神秘⬅️
            {'t': 'click', 'p': (532, 479), 'ec': True}, {'t': 'click', 'p': (596, 386), 'ec': False, 'wait': 7},
            # 神秘↗️   爆发⬅️
            {'t': 'click', 'p': (597, 230), 'ec': True}, {'t': 'click', 'p': (545, 429), 'ec': True, 'wait': 3},
            # 神秘➡️  爆发↖️Boss
            {'t': 'click', 'p': (801, 280), 'ec': True, 'wait': 2}, {'t': 'click', 'p': (492, 398), 'ec': False},
        ]
    }
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus', mis_fu=self.click, mis_argv=(1195, 576))

    # 点击任务
    self.click(816, 285)

    # 选择地点加载
    image.compare_image(self, 'normal_task_menu', 20, 3, False, home.click_house_under, (self,))

    if self.tc['task'] == 'hard_task':
        # 点击困难
        while not color.check_rgb_similar(self, (1000, 150, 1001, 151), (66, 66, 198)):
            self.click(1062, 154)
    else:
        # 点击普通
        while not color.check_rgb_similar(self, (700, 150, 701, 151), (88, 66, 46)):
            self.click(803, 156)
    # 开始战斗
    for region in self.tc['config']['region']:
        start_fight(self, region)

    # 回到首页
    home.go_home(self)


def start_fight(self, region):
    # 选择区域
    choose_region(self, region)
    gk = region_scheck_scan(self, region)
    if gk is None:
        self.logger.info("本区域没有需要开图的任务关卡...")
        return
    # 点击开始任务
    self.click(947, 540)
    # 等待地图加载

    # 遍历start需要哪些队伍
    start_choose_team(self, gk, '1')
    start_choose_team(self, gk, '2')
    image.compare_image(self, 'normal_task_fight-task')
    # 点击开始任务
    self.click(1172, 663)
    # 检查跳过战斗
    image.compare_image(self, 'normal_task_fight-skip', mis_fu=self.click, mis_argv=(1123, 545), rate=2)
    # 检查回合自动结束
    image.compare_image(self, 'normal_task_auto-over', mis_fu=self.click, mis_argv=(1082, 599), rate=2)
    # 开始战斗
    start_action(self, gk)
    # 自动战斗
    main_story.auto_fight(self)
    # 任务完成
    self.click(1036, 660)
    # 关闭获得奖励
    self.click(771, 655)


def region_scheck_scan(self, region):
    # 选择第一关
    self.click(1118, 239)
    while True:
        # 等待任务信息加载
        image.compare_image(self, 'normal_task_task-info')
        if self.tc['config']['mode'] == 1:
            # 点击下一关
            self.click(1167, 357)
            # 等待任务信息加载
            image.compare_image(self, 'normal_task_task-info')
            gk = get_stage(self, region)
            if gk is None:
                self.logger.info("本区域已全部解锁成功")
                return
            if gk == 'sq':
                return gk
            continue
        # 判断是否可以扫荡
        if image.compare_image(self, 'normal_task_task-scan', 3):
            # 点击下一关
            self.click(1167, 357)
            continue
        gk = get_stage(self, region)
        if stage is None:
            # todo 应该是支线战队
            pass
        if gk not in stage_data:
            self.logger.critical("本关卡{0}尚未支持开图，正在全力研发中...".format(gk))
            sys.exit(1)
        return gk
    return None


def get_stage(self, region):
    for i in range(1, 6):
        s = '{0}-{1}'.format(region, i)
        if image.compare_image(self, 'normal_task_' + s, 0):
            return s
    if image.compare_image(self, 'normal_task_side-quest', 0):
        return 'sq'
    return None


def get_force(self):
    for i in range(1, 5):
        if image.compare_image(self, 'normal_task_force-{0}'.format(i), 0):
            return i


def start_action(self, gk):
    for i, act in enumerate(stage_data[gk]['action']):
        # 获取当前部队编号队伍
        force_index = get_force(self)
        self.logger.info("开始 {0} 次行动".format(i + 1))
        if act['t'] == 'click':
            # 行动
            self.click(*act['p'])
        elif act['t'] == 'exchange':
            self.logger.info("更换部队")
            self.click(83, 557)
        # 判断是否存在exchange事件
        if act['ec']:
            # 等待换队
            image.compare_image(self, 'normal_task_force-{0}'.format(force_index), n=True)
        # 行动后置等待时间
        if 'wait' in act:
            self.logger.info("后置等待{0}秒".format(act['wait']))
            time.sleep(act['wait'])
        time.sleep(0.5)


def start_choose_team(self, gk, force):
    image.compare_image(self, 'normal_task_fight-task')
    # 点击开始按钮
    time.sleep(1)
    self.double_click(*stage_data[gk]['start'][force])
    # 等待编队加载
    image.compare_image(self, 'normal_task_force-edit')
    # 选择对应属性的队伍
    fp = force_position[self.tc['config'][stage_data[gk]['attr'][force]]]
    time.sleep(1)
    self.double_click(*fp)
    # todo 检查是否选中了
    # 等待队伍加载
    time.sleep(3)
    # 点击出击
    self.click(1163, 658)


def choose_region(self, region):
    cu_region = int(ocr.screenshot_get_text(self, (122, 178, 163, 208), self.ocrNum))
    if cu_region == region:
        return
    elif cu_region > region:
        self.click(40, 360)
    else:
        self.click(1245, 360)
    return choose_region(self, region)
