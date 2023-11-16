import time

from modules.baas import home
from common import ocr, stage, image

x = {
    'menu': (107, 9, 162, 36),
    'buy3': (682, 311, 714, 327),
    'buy2': (682, 311, 714, 327),
    'buy1': (682, 311, 714, 327),
    'confirm': (737, 446, 766, 476)
}
render = {
    "base": {
        "name": "功能设置"
    },
    'config': {
        'name': '购买设置'
    },
    'config.count': {
        "type": "num",
        "name": "购买次数",
        "desc": "默认可购买一次+刷新次数=购买次数，比如购买2次=默认买1次+刷新购买1次",
        "opts": {
            "min": 1,
            "max": 4,
            "step": 1
        }
    },
    'config.enable': {
        "type": "bool",
        "name": "启用该功能"
    },
    "config.shop": {
        "type": "sel",
        "name": "商店",
        "items": [
            {
                "value": "general",
                "name": "常规道具"
            }, {
                "value": "arena",
                "name": "战术对抗赛"
            }
        ]
    },
    "config.goods": {
        "type": "sel",
        "name": "道具序号",
        "desc": "从左往右，从上往下的顺序数",
        "opts": {
            "multiple": "true"
        },
        "items": {
            "min": 1,
            "max": 16,
            "step": 1
        }
    },
}
shop_position = {
    'general': (150, 150), 'arena': (150, 380)
}

goods_position = {
    1: (650, 200), 2: (805, 200), 3: (960, 200), 4: (1110, 200),
    5: (650, 460), 6: (805, 460), 7: (960, 460), 8: (1110, 460),
    9: (650, 160), 10: (805, 160), 11: (960, 160), 12: (1110, 160),
    13: (650, 420), 14: (805, 420), 15: (960, 420), 16: (1110, 420),
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击商店
    self.double_click(821, 651)
    # 等待商店页面加载
    image.compare_image(self, 'shop_menu')
    # 购买商品
    buy_goods(self)
    # 回到首页
    home.go_home(self)


def refresh_shop(self, shop):
    """
    刷新商店
    """
    need_count = shop['count']
    purchased_count = 4 - calc_surplus_count(self)
    # 次数已满
    if need_count <= purchased_count:
        # 关闭购买弹窗
        home.click_house_under(self)
        return False
    # 点击购买
    self.click(765, 460, False)
    return True


def calc_surplus_count(self):
    """
    计算剩余购买次数,这里必须用图片匹配才能精准,用文字识别小数字必出bug
    """
    self.click(945, 659, False)
    # 等待确认购买加载
    if not image.compare_image(self, 'shop_confirm', 10):
        # 未能加载还剩0次
        return 0
    for i in range(3, 0, -1):
        if image.compare_image(self, 'shop_buy{0}'.format(i), 0):
            return i
    return 0


def buy_goods(self):
    """
    刷新并购买商品
    """
    for shop in self.tc['config']:
        if not shop['enable']:
            continue
        self.double_click(*shop_position[shop['shop']], False)
        start_buy(self, shop)
        while refresh_shop(self, shop):
            start_buy(self, shop)


def start_buy(self, shop):
    """
    开始购买商品
    """
    # 选择商品
    choose_goods(self, shop['goods'])

    if not ocr.screenshot_check_text(self, '选择购买', (1116, 645, 1213, 676), 0):
        self.logger.info("没有选中道具")
        return

    # 点击选择购买
    self.click(1164, 660, False)

    # 等待确认购买页面
    ocr.screenshot_check_text(self, '是否购买', (581, 229, 698, 264))

    # 确认购买
    self.click(769, 484, False)

    # 关闭获得奖励
    stage.close_prize_info(self, True)


def choose_goods(self, goods):
    swipe = False
    # todo 商品渲染需要时间...
    time.sleep(0.5)
    self.logger.info("开始点击所需商品")
    for g in goods:
        if g > 8 and not swipe:
            swipe = True
            self.swipe(933, 586, 933, 230)
            self.swipe(933, 586, 933, 230)
            time.sleep(0.5)
        # 点击商品,防止太快点不到
        time.sleep(0.2)
        self.click(*goods_position[g], False)
