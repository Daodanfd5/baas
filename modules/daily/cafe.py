import time
from collections import defaultdict
import numpy as np
from common import stage, ocr, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36),
    '0.0': (1114, 642, 1155, 665)
}
preset_position = {
    1: (808, 263), 2: (808, 393), 3: (808, 533), 4: (812, 393), 5: (812, 523)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 初始化窗口
    init_window(self)
    # 领取收益
    get_cafe_money(self)
    # 邀请妹子
    invite_girl(self)
    # 和妹子互动
    start_interactive(self)
    # 回到首页
    home.go_home(self)


def start_interactive(self):
    preset = self.tc['config']['blank_preset']
    load_preset(self, preset)
    # 收起菜单
    time.sleep(0.2)
    self.double_click(555, 622, False)
    i = 3
    while i > 0:
        click_girl_plus(self, i)
        if ocr.screenshot_check_text(self, '好感等级提升', (473, 593, 757, 644), 3):
            # 关闭好感窗口,重新开始
            self.double_click(651, 285, False)
            time.sleep(0.5)
            i = 3
            continue
        i -= 1
    # 暂开菜单
    self.click(57, 624, False)
    # 恢复玩家原有预设
    recover_preset(self, preset)


def recover_preset(self, preset):
    # 恢复玩家原有预设
    open_preset_window(self, preset)
    self.click(*preset_position[preset], False)
    confirm_load_preset(self)


def load_preset(self, preset):
    open_preset_window(self, preset)
    # 保存当前配置到配置中预设
    save_preset(self, preset)
    # 点击全部收纳
    self.click(455, 642, False, 1, 0.5)
    # 等待确认加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认收纳
    self.click(769, 498, False)


def open_preset_window(self, preset):
    # 等待右下角预设
    ocr.screenshot_check_text(self, '预设', (326, 656, 366, 677))
    # 点击右下角预设
    self.click(360, 640)
    # 等待预设弹窗加载
    ocr.screenshot_check_text(self, '预设', (604, 127, 678, 157))
    if preset > 3:
        self.swipe(933, 586, 933, 230)
        time.sleep(0.5)


def create_blank_preset(self, preset):
    # 把当前配置保存到空白预设
    save_preset(self, preset)
    # 点击全部收纳
    self.click(455, 642, False, 1, 0.5)
    # 等待确认加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认收纳
    self.click(769, 498, False)
    # 重新打开预设
    open_preset_window(self, preset)
    # 保存预设
    save_preset(self, preset)
    # 等待加载
    ocr.screenshot_check_text(self, '制造工坊', (732, 482, 803, 518), 0, 0, False)
    # 点击确认
    self.click(769, 498, False)


def save_preset(self, preset):
    area = preset_position[preset]
    # 点击保存当前配置
    self.click(area[0] - 250, area[1], False)
    # 确认加载预设
    confirm_load_preset(self)


def confirm_load_preset(self):
    # 等待加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认加载
    self.click(771, 500, False)
    # 等待预设弹窗加载
    ocr.screenshot_check_text(self, '预设', (604, 127, 678, 157))
    # 关闭预设
    self.double_click(934, 146, False)


def init_window(self):
    # 点击咖啡厅
    self.double_click(89, 653)
    # 等待进入咖啡厅
    image.compare_image(self, 'cafe_menu', 999, 10, False, self.click, (919, 186, False))
    # 双指捏合
    sx1, sy1 = 1000, 330
    sx2, sy2 = 800, 330
    ex1, ey1 = 150, 330
    ex2, ey2 = 150, 330
    self.d().gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))
    # 拖到最左边
    self.swipe(392, 564, 983, 82)


def invite_girl(self):
    if not ocr.screenshot_check_text(self, "可以使用", (801, 586, 875, 606), 0):
        return
    # 点击邀请券
    self.click(830, 640)
    # 等待加载邀请
    ocr.screenshot_check_text(self, "邀请", (760, 200, 815, 236))
    # 邀请第一个
    self.click(787, 221)
    # 等待确认加载
    ocr.screenshot_check_text(self, "确认", (727, 480, 805, 519))
    # 点击确认
    self.click(770, 500)
    # 强制等待发消息邀请妹子
    time.sleep(3)


def get_cafe_money(self):
    # 查看是否需要领取体力
    if not self.tc['config']['receive_ap']:
        return
    # 查看收益
    if image.compare_image(self, 'cafe_0.0', 0):
        return
    # 点击咖啡厅收益
    self.click(1155, 645)
    # 等待领取
    ocr.screenshot_check_text(self, "领取", (600, 500, 678, 538))
    # 点击领取
    self.click(641, 516)
    # 关闭获得奖励
    stage.close_prize_info(self, True)
    # 关闭领取界面
    self.click(903, 155, False)
    # 防止体力超出
    self.click(903, 155, False)


def click_girl_plus(self, i):
    if i % 2 == 0:
        self.swipe(327, 512, 1027, 125)
    else:
        self.swipe(1008, 516, 300, 150)
    time.sleep(0.5)
    before = self.d.screenshot()
    time.sleep(1)
    after = self.d.screenshot()
    # 将图像转换为numpy数组以便进行数学操作
    img1_data = np.array(before)
    img2_data = np.array(after)

    diff_pixels_coords = np.where(img1_data != img2_data)
    # 创建一个映射，键是每个像素点所在的50px区块的坐标，值是该区块中所有不同像素点的列表
    blocks = defaultdict(list)

    for p in zip(*diff_pixels_coords):
        x = int(p[1])
        y = int(p[0])
        # 计算此像素所在的区块坐标
        block_coord = (y // 50, x // 50)
        blocks[block_coord].append((y, x))

    # 对于每个区块，保留中间的像素点
    finial = []
    for block_coord, pixels in blocks.items():
        # 将像素列表按照Y和X排序
        pixels.sort()
        # 取出中间的像素
        mid_pixel = pixels[len(pixels) // 2]
        # 将坐标变换回原图尺寸
        center_coord = (mid_pixel[0] * 1 + 0.5, mid_pixel[1] * 1 + 0.5)
        # 防止溢出到功能按钮
        x = int(center_coord[1])
        y = int(center_coord[0])
        if y < 70 or \
                (y < 130 and x < 320) or (y < 130 and x > 1170) or \
                (y > 570 and x < 100) or (y > 570 and x > 770):
            continue
        finial.append(center_coord)
    # 打乱坐标
    np.random.shuffle(finial)
    for p in finial:
        self.click(int(p[1]), int(p[0]), False)
