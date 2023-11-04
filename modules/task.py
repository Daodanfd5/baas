from modules import home
from utils import ocr


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击工作任务
    self.double_click(62, 236)
    # 等待工作任务页面加载
    ocr.is_task(self)

    while True:
        if ocr.check_rgb_similar(self):
            print("开始领取奖励")
            # 点击一键领取
            self.click(1136, 669)
            # 关闭获得奖励
            ocr.close_prize_info(self)
            # 点击空白处防止体力超出
            self.click(1236, 79)
        else:
            print("没有需要领取的奖励")
            break

    # 返回首页
    home.click_house(self)
