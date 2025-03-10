import importlib
import time

from common import ocr, color, stage, image
from modules.baas import home
from modules.scan import main_story

x = {
}
# 普通关卡坐标
normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}
# 部队1234坐标
force_position = {
    1: (124, 195), 2: (124, 277), 3: (124, 354), 4: (124, 429),
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
        self.stage_data = get_stage_data(self, region)
        if self.stage_data is None:
            continue
        start_fight(self, region)

    # 回到首页
    home.go_home(self)


def start_fight(self, region):
    # 选择区域
    choose_region(self, region)
    gk = calc_need_fight_stage(self, region)
    if gk is None:
        self.logger.critical("本区域没有需要开图的任务关卡...")
        return
    # 点击开始任务
    if gk == 'side':
        self.click(645, 511)
    else:
        if gk not in self.stage_data:
            self.logger.critical("本关卡{0}尚未支持开图，正在全力研发中...".format(gk))
            return
        self.click(947, 540)
    # 等待地图加载

    # 遍历start需要哪些队伍
    if gk == "side":
        # 选择支线部队开始战斗
        start_choose_side_team(self, self.stage_data[str(region)]['side'])
        # 自动战斗
        main_story.auto_fight(self)
    else:
        for n, p in self.stage_data[gk]['start'].items():
            start_choose_team(self, gk, n)
        image.compare_image(self, 'normal_task_fight-task')
        # 点击开始任务
        self.click(1172, 663)
        time.sleep(3)
        # 检查跳过战斗
        image.compare_image(self, 'normal_task_fight-skip', threshold=10, mis_fu=self.click, mis_argv=(1123, 545),
                            rate=2)
        # 检查回合自动结束
        image.compare_image(self, 'normal_task_auto-over', threshold=10, mis_fu=self.click, mis_argv=(1082, 599),
                            rate=2)
        # 开始战斗
        start_action(self, gk, self.stage_data)
        # 自动战斗
        main_story.auto_fight(self)
        # 等待任务完成
        image.compare_image(self, 'normal_task_task-finish')
        # 确认(任务完成)
        time.sleep(1)
        self.double_click(1038, 662, )
    # 等待获得奖励
    image.compare_image(self, 'normal_task_prize-confirm')
    # 点击确认
    self.double_click(776, 655)
    # 选择地点加载
    image.compare_image(self, 'normal_task_menu')
    # 往左一个区域
    choose_region(self, region - 1)
    # 重新开始本区域探索
    return start_fight(self, region)


def get_stage_data(self, region):
    # 动态生成完整的模块路径
    module_path = f'modules.exp.normal_task.stage_data.nt_{region}'
    # 导入指定的模块
    try:
        stage_module = importlib.import_module(module_path)
        stage_data = getattr(stage_module, 'stage_data', None)
        # 从该模块中获取stage_data数据
        return stage_data
    except ModuleNotFoundError:
        self.logger.critical("当前区域 {0} 尚未支持开图，正在全力研发中...".format(region))
        return None


def check_task_state(self):
    """
    检查任务当前类型
    @param self:
    @return:
    """
    # 等待任务信息弹窗加载
    wait_task_info(self)
    time.sleep(1)
    # 主线-三星
    if image.compare_image(self, 'normal_task_task-scan', 0):
        return 'sss'
    # 主线-未通关
    if image.compare_image(self, 'normal_task_no-pass', 0):
        return 'no-pass'
    # 支线任务-未通关
    if image.compare_image(self, 'normal_task_side-quest', 0):
        return 'side'
    # 主线-已通关
    return 'pass'


def wait_task_info(self, open_task=False, max_retry=99999):
    """
    等待任务信息弹窗加载
    @param self:
    @return:
    """
    while max_retry > 0:
        # 主线任务
        if image.compare_image(self, 'normal_task_task-info', 0):
            return 'main'
        # 支线任务
        if image.compare_image(self, 'normal_task_side-quest', 0):
            return 'side'
        time.sleep(0.1)
        # 是否要打开入场
        if open_task:
            self.click(1118, 239)
            time.sleep(1)
        max_retry -= 1
        self.logger.error("max_retry {0}".format(max_retry))
    return None


def calc_need_fight_stage(self, region):
    """
    查找需要战斗的关卡
    @param self:
    @param region:
    @return:
    """
    wait_task_info(self, True)
    fail = 0
    while True:
        # 等待任务信息加载
        task_state = check_task_state(self)
        task_state = 'no-pass'
        self.logger.info("当前关卡状态为:{0}".format(task_state))
        # 未通关支线
        if task_state == 'side':
            self.logger.info("开始支线战斗")
            return task_state
        # 未通关主线 or 要求三星但未三星
        if task_state == 'no-pass' or (self.tc['config']['mode'] == 2 and task_state != 'sss'):
            self.logger.info("开始主线战斗")
            return get_stage(self, region)
        # 点击下一关
        self.logger.warn("不满足战斗条件,查找下一关")
        self.click(1172, 358)
        # 检测是否还在本区域
        fail += 1
        if fail >= 5:
            time.sleep(1)
            if region != ocr.screenshot_get_text(self, (189, 197, 228, 225), self.ocrNum):
                return None


def get_stage(self, region):
    for i in range(1, 6):
        s = '{0}-{1}'.format(region, i)
        try:
            if image.compare_image(self, 'normal_task_' + s, 0):
                return s
        except KeyError:
            self.logger.critical("当前关卡{0}尚未支持开图，正在全力研发中...".format(s))
            return None
    return None


def get_force(self):
    fail = 0
    while True:
        for i in range(1, 5):
            if image.compare_image(self, 'normal_task_force-{0}'.format(i), 0):
                return i
        if fail > 0:
            self.logger.info("图片识别部队失败，开始OCR识别...")
            i = ocr.screenshot_get_text(self, (118, 548, 130, 564), self.ocrNum, 2)
            if i == "":
                continue
            try:
                i = int(i)
                if 0 < i < 5:
                    return i
            except Exception:
                pass
        fail += 1


def start_action(self, gk, stage_data):
    force_index = 0
    for i, act in enumerate(stage_data[gk]['action']):
        # 行动前置等待时间
        if 'before' in act:
            self.logger.info("前置等待{0}秒".format(act['before']))
            time.sleep(act['before'])
        # 每次行动强制等1s
        time.sleep(1)
        self.logger.info("开始 {0} 次行动".format(i + 1))
        # 获取当前部队编号队伍(移动部队这种弹框不能重新计算,因为他有个遮罩)
        if act['t'] != 'move':
            force_index = get_force(self)

        if act['t'] == 'click':
            self.click(*act['p'])
        elif act['t'] == 'exchange':
            self.logger.info("更换部队")
            self.click(83, 557)
        elif act['t'] == 'move':
            self.logger.info("确认移动部队")
            image.compare_image(self, 'normal_task_move-force-confirm')
            # 确认移动
            self.click(771, 495)
            time.sleep(2)

        # 判断是否存在exchange事件
        if 'ec' in act:
            # 等待换队
            self.logger.info("等待队伍更换事件...")
            image.compare_image(self, 'normal_task_force-{0}'.format(force_index), n=True)

        # 行动后置等待时间
        if 'after' in act:
            self.logger.info("后置等待{0}秒".format(act['after']))
            time.sleep(act['after'])

        if 'wait-over' in act:
            self.logger.info("等待战斗结束...")
            # 一直点击任务信息，直到任务信息出现
            image.compare_image(self, 'normal_task_fight-task-info', mis_fu=self.click, mis_argv=(1003, 666), rate=1)
            # 任务信息出现后一直点击最上方，直到消失
            image.compare_image(self, 'normal_task_fight-task-info', mis_fu=self.click, mis_argv=(529, 25), n=True)
        stage.wait_loading(self)


def start_choose_side_team(self, team):
    # 选择对应属性的队伍
    select_force_fight(self, self.tc['config'][team])


def select_force_fight(self, index):
    """
    选择队伍并开始战斗
    @param self:
    @param index: 队伍索引
    """
    self.logger.info("根据当前配置,选择部队{0}".format(index))
    if index == -1:
        self.exit("你没有未配置部队,请根据开图区域设置对应属性的部队编号")
    fp = force_position[index]
    # 检查是否有选中,直到选中为止
    while not color.check_rgb_similar(self, (fp[0], fp[1], fp[0] + 1, fp[1] + 1), (105, 74, 50)):
        self.click(*fp)
        time.sleep(1)
    # 点击出击 直到没有出击
    time.sleep(1)
    image.compare_image(self, 'normal_task_attack', threshold=50, mis_fu=self.click, mis_argv=(1163, 658), rate=1,
                        n=True)


def start_choose_team(self, gk, force):
    image.compare_image(self, 'normal_task_fight-task')
    # 点击开始按钮
    time.sleep(1)
    self.double_click(*self.stage_data[gk]['start'][force])
    # 等待编队加载
    image.compare_image(self, 'normal_task_force-edit')
    # 选择对应属性的队伍
    select_force_fight(self, self.tc['config'][self.stage_data[gk]['attr'][force]])


def choose_region(self, region):
    cu_region = int(ocr.screenshot_get_text(self, (122, 178, 163, 208), self.ocrNum))
    if cu_region == region:
        return
    elif cu_region > region:
        self.click(40, 360)
    else:
        self.click(1245, 360)
    return choose_region(self, region)
