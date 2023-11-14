import time

from common import ocr, color, stage, image
from modules.baas import home, cm
from modules.scan import hard_task

x = {
    'menu': (107, 9, 162, 36),
}
normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus')

    # 点击任务
    self.click(816, 285)

    # 选择地点加载
    image.compare_image(self, 'normal_task_menu')

    # 关闭主线剧情解锁
    image.compare_image(self, 'cm_notice', 5, 3, False, home.click_house_under, (self,))

    if self.tc['task'] == 'hard_task':
        # 点击困难
        while not color.check_rgb_similar(self, (1000, 150, 1001, 151), (66, 66, 198)):
            self.click(1062, 154)
    else:
        # 点击普通
        while not color.check_rgb_similar(self, (700, 150, 701, 151), (88, 66, 46)):
            self.click(803, 156)
    # 开始扫荡
    start_scan(self)

    # 回到首页
    home.go_home(self)


def start_scan(self):
    prev_region = None
    swipe = False
    for tk in self.tc['config']:
        # 选择区域
        choose_region(self, tk['region'])
        if self.tc['task'] == 'hard_task':
            # 点击入场
            self.click(*hard_task.hard_position[tk['stage']])
        else:
            if prev_region == tk['region'] and swipe:
                self.swipe(933, 230, 933, 586)
                time.sleep(0.5)
            if tk['stage'] > 4:
                self.swipe(933, 586, 933, 230)
                time.sleep(0.5)
            prev_region = tk['region']
            swipe = tk['stage'] > 4
            # 点击入场
            self.click(*normal_position[tk['stage']])
        # 确认扫荡
        rst = stage.confirm_scan(self, tk)
        if rst == 'return':
            return
        # 关闭任务信息
        self.double_click(1236, 98)


def choose_region(self, region):
    cu_region = int(ocr.screenshot_get_text(self, (122, 178, 163, 208), self.ocrNum))
    if cu_region == region:
        return
    elif cu_region > region:
        self.click(40, 360)
    else:
        self.click(1245, 360)
    return choose_region(self, region)
