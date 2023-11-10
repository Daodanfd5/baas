from common import ocr, image
from modules.baas import home

x = {
    'entry': (1172, 172, 1210, 205)
}


def start(self):
    # 回到首页
    home.go_home(self)

    # 等待活动页加载
    image.compare_image(self, 'tutor_dept_entry', 999)

    # 点击活动页
    self.d.click(1191, 198)

    # 回到首页
    home.go_home(self)
