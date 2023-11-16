from common import ocr, image
from modules.baas import home
from modules.daily import special_entrust

x = {
}
render = {
    "base": {
        "name": "功能设置"
    },
    'config': {
        'name': '关卡设置'
    },
    "config.stage": {
        "type": "sel",
        "name": "关卡",
        "desc": "从左往右，从上往下的顺序数",
        "items": {
            "min": 1,
            "max": 8,
            "step": 1
        }
    },
    'config.count': {
        "type": "num",
        "name": "扫荡次数",
        "desc": "可指定1-99次，次数比较小的时候点击比较慢，99次会高频点击用光所有体力",
        "opts": {
            "min": 1,
            "max": 99,
            "step": 10
        }
    },
    "config.entrust": {
        "type": "sel",
        "name": "委托",
        "items": [
            {
                "value": "gjgl",
                "name": "高架公路"
            },
            {
                "value": "smtl",
                "name": "沙漠铁路"
            },
            {
                "value": "jt",
                "name": "讲堂"
            }
        ]
    },
}
entrust_position = {
    'gjgl': (950, 270), 'smtl': (950, 415), 'jt': (950, 550)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus')

    # 点击悬赏通缉
    self.click(733, 472)
    # 选择委托
    special_entrust.choose_entrust(self, entrust_position)
    # 回到首页
    home.go_home(self)
