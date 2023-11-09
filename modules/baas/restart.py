import time

from common import ocr
from modules.baas import home


def start(self):
    # 重启应用
    pkg = self.bc['baas']['package']
    self.d.app_stop(pkg)
    self.d.app_start(pkg)
    # 强制等待
    time.sleep(8)
    # 重新进入登录页面
    ocr.is_login(self)
    # 点击登录
    self.double_click(500, 500)
    # 重新判断是否进入首页
    while True:
        if home.is_home(self):
            break
        # 检查跳过
        if ocr.screenshot_check_text(self, '通知', (599, 144, 675, 178), 3):
            # 确认跳过
            self.d.click(770, 500)
            continue
        # 关闭签到
        self.click(661, 88)
        time.sleep(0.5)
