import time

from common import image
from modules.baas import restart

x = {
    'cafe': (88, 651, 96, 657),  # 咖啡厅
    'bus': (107, 9, 162, 36),  # 业务区
}


def is_home(self):
    """
    是否为首页
    """
    return image.compare_image(self, 'home_cafe', 0)


def go_home(self):
    """
    回到首页
    """
    app = self.d.app_current()
    if app['package'] != self.bc['baas']['package']:
        # 启动游戏
        return restart.start(self)
    # 返回首页
    if recursion_click_house(self):
        return
    # 返回首页失败启动游戏
    restart.start(self)


def click_house_under(self):
    self.double_click(1236, 67, False)


def recursion_click_house(self, check_text=False, fail_count=0):
    """
    递归点击首页按钮，如果返回False则返回首页失败，反之返回首页成功
    """
    # 多次返回失败
    if fail_count >= 30:
        self.logger.info("多次返回首页失败! 开始重启")
        return False
    if is_home(self):
        # 在首页先点击右上角
        self.click(1233, 11, False)
        # 和妹子互动
        self.double_click(851, 262, False)
        return True
    # 返回首页
    self.double_click(1233, 11, False)
    # 重新检查
    time.sleep(self.bc['baas']['ss_rate'])
    return recursion_click_house(self, check_text, fail_count + 1)
