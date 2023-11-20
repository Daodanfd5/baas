from common import image

x = {
    'notice': (610, 146, 640, 175),
    'skip-menu': (1177, 27, 1228, 51),
    'confirm': (737, 505, 797, 535)
}
render = {
    "base.enable": {
        "type": "bool",
        "name": "启用该功能",
        "desc": "将这个任务加入调度器"
    },
    "base.next": {
        "type": "txt",
        "name": "下一次运行时间",
        "desc": "自动计算的数值，不需要手动修改。清空后将立即运行"
    },
    "base.end": {
        "type": "txt",
        "name": "任务截止时间",
        "desc": "超出该时间的任务不会执行。不填则永不停止"
    },
    "base.index": {
        "type": "num",
        "name": "任务优先级",
        "desc": "数字越低，越先执行"
    },
    "base.interval": {
        "type": "num",
        "name": "再次执行任务时间",
        "desc": "完成任务后，间隔多少秒后重复执行任务，填0：表示明天再执行 填3600：表示1小时候再执行"
    },
    "base.link_task": {
        "type": "sel",
        "name": "关联任务",
        "desc": "完成本任务后，立刻执行关联任务",
        "items": [
            {
                "value": "",
                "name": "不关联"
            },
            {
                "value": "restart",
                "name": "重启"
            }, {
                "value": "buy_ap",
                "name": "购买体力"
            }, {
                "value": "group",
                "name": "小组"
            }, {
                "value": "tutor_dept",
                "name": "补习部签到"
            }, {
                "value": "make",
                "name": "制造"
            }, {
                "value": "schedule",
                "name": "日程"
            }, {
                "value": "shop",
                "name": "商店购买"
            }, {
                "value": "cafe",
                "name": "咖啡厅"
            }, {
                "value": "arena",
                "name": "战术对抗赛"
            }, {
                "value": "special_entrust",
                "name": "特殊委托"
            }, {
                "value": "wanted",
                "name": "通缉悬赏"
            }, {
                "value": "mailbox",
                "name": "领取邮箱"
            }, {
                "value": "momo_talk",
                "name": "MomoTalk"
            }, {
                "value": "work_task",
                "name": "工作任务"
            }, {
                "value": "normal_task",
                "name": "扫荡普通关卡"
            }, {
                "value": "hard_task",
                "name": "扫荡困难关卡"
            }
        ]
    },
    "base.text": "skip"
}


def close_notice(self):
    """
    关闭通知
    @param self:
    """
    if image.compare_image(self, 'cm_notice', 3):
        self.click(888, 160, False)
