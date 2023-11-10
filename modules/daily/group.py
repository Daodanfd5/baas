from common import ocr, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击小组
    self.double_click(578, 648)
    # 等待小组页面加载
    image.compare_image(self, 'group_menu')
    # 检查签到奖励
    if ocr.screenshot_check_text(self, "确认", (600, 468, 682, 506), 0):
        self.click(641, 485)
    # 回到首页
    home.go_home(self)
