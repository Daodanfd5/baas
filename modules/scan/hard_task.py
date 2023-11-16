from modules.scan import normal_task

x = {
}
render = {
    "base": {
        "name": "功能设置"
    },
    'config': {
        'name': '关卡设置'
    },
    "config.region": {
        "type": "sel",
        "name": "区域",
        "opts": {
            "min": 4,
            "max": 20,
            "step": 1
        }
    },
    "config.stage": {
        "type": "sel",
        "name": "关卡",
        "desc": "从上往下的顺序数",
        "items": {
            "min": 1,
            "max": 3,
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
    }
}
hard_position = {
    1: (1120, 250), 2: (1120, 370), 3: (1120, 480),
}


def start(self):
    normal_task.start(self)
