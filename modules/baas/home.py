from common import image
from modules.baas import restart

x = {
    'lt': (10, 24, 20, 34),  # 左上角蓝色区域
}


def is_home(self):
    """
    是否为首页
    """
    return image.compare_image(self, 'home_lt')


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


def recursion_click_house(self, check_text=False, fail_count=0):
    """
    递归点击首页按钮，如果返回False则返回首页失败，反之返回首页成功
    """
    # 多次返回失败
    if fail_count >= 5:
        return False
    if is_home(self):
        # 在首页先点击右上角
        self.d.click(1233, 11)
        # 和妹子互动
        self.d.double_click(851, 262)
        return True
    # 返回首页
    self.d.double_click(1233, 11)
    # 重新检查
    return recursion_click_house(self, check_text, fail_count + 1)
