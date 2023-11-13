import time

from common import ocr, image
from modules.baas import home

x = {
    'menu': (38, 628, 75, 646),
    'maintain': (604, 301, 654, 327)
}


def start(self):
    # 重启应用
    pkg = self.bc['baas']['package']
    self.d.app_stop(pkg)
    self.d.app_start(pkg)
    # 强制等待
    time.sleep(8)
    # 重新进入登录页面
    image.compare_image(self, 'restart_menu')
    # 点击登录
    self.double_click(500, 500)
    # 重新判断是否进入首页
    while True:
        if home.is_home(self):
            break
        # 检查维护
        if image.compare_image(self, 'restart_maintain', 0):
            self.d.click(640, 500)
            self.logger.info("维护中......")
            time.sleep(60)
            continue
        # 检查跳过live2d
        if ocr.screenshot_check_text(self, '通知', (599, 144, 675, 178), 0, 0, False):
            # 确认跳过
            self.d.click(770, 500)
            continue
        # 关闭签到或公告
        self.d.double_click(1233, 11)
        time.sleep(self.bc['baas']['ss_rate'])
