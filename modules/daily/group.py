from common import ocr, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36)
}
render = {}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击小组
    self.double_click(578, 648)
    # 等待小组页面加载,关闭签到奖励
    image.compare_image(self, 'group_menu', 999, 10, False, self.click, (641, 485, False))
    # 回到首页
    home.go_home(self)
