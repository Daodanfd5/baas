from common import ocr, config
import os
import time
from fuzzywuzzy import fuzz

from modules.baas import home


def confirm_scan(self, tk):
    # 等关卡加载
    ocr.screenshot_check_text(self, '任务信息', (574, 122, 709, 155))
    if tk['count'] >= 99:
        self.double_click(1034, 299, False, 20)
    else:
        # 扫荡指定次数
        self.click(1034, 299, False, tk['count'] - 1, 0.6)
    # 点击开始扫荡
    self.click(938, 403, False)
    # 判断困难次数
    if self.tc['task'] == 'hard_task':
        # 查看次数是否足够
        if ocr.screenshot_check_text(self, '是否恢复挑战次数', (522, 251, 729, 279), 0, 0.5):
            self.double_click(1236, 98, False)
            return 'continue'
    # 判断统计悬赏票数
    if self.tc['task'] == 'wanted':
        # 查看入场券是否足够
        if ocr.screenshot_check_text(self, '移动', (730, 485, 803, 516), 0, 0.5):
            # 下一个
            self.click(56, 38, 0, 3)
            return 'continue'
    else:
        # 查看体力是否足够
        if ocr.screenshot_check_text(self, '是否购买', (515, 227, 627, 260), 0, 0.5):
            # 关闭弹窗 返回首页
            home.go_home(self)
            return 'return'

    # 等待确认加载
    ocr.screenshot_check_text(self, '通知', (599, 144, 675, 178))
    # 确认扫荡
    self.click(770, 500, False)
    # 检查跳过,最多检查30次
    if tk['count'] >= 3:
        ocr.screenshot_check_text(self, '跳过', (600, 488, 684, 526), 30)
        # 点击跳过
        self.click(641, 504, False)
    # 等待结算,这里很有可能会升级点击关闭升级弹窗
    while not ocr.screenshot_check_text(self, '确认', (597, 562, 680, 600), 0):
        self.click(850, 582, False)
        time.sleep(1)
    # 确认奖励
    self.click(641, 580, False)
    return 'nothing'


def close_prize_info(self, ap_check=False, mail_check=False):
    """
    关闭奖励道具结算页面
    """
    if ocr.screenshot_check_text(self, '点击继续', (577, 614, 704, 648), 1):
        # 关闭道具信息
        self.click(640, 635)
        time.sleep(0.5)
        return
    if ap_check and ocr.screenshot_check_text(self, '因超出持有上限', (532, 282, 724, 314), 1):
        self.click(650, 501)
        return
    if mail_check and ocr.screenshot_check_text(self, '以上道具的库存已满', (508, 388, 745, 419), 1):
        self.click(642, 527)
        return
    return close_prize_info(self, ap_check, mail_check)


def wait_loading(self):
    """
    检查是否加载中，
    """
    ss_path = config.get_ss_path(self)
    if not os.path.exists(ss_path):
        os.makedirs(ss_path)
    ss = self.d.screenshot()
    img = ss.crop((925, 650, 1170, 685))
    img.save(config.get_ss_path(self))
    out = self.ocrEN.ocr(config.get_ss_path(self))
    text = "Now Loading"
    ex = any(map(lambda d: fuzz.ratio(d.get('text'), text) > 20, out))

    self.logger.info("wait_loading Text:%s Result:%s", text, ex)
    # 如果找到加载继续等待
    if ex:
        self.logger.info("Now Loading......")
        time.sleep(self.bc['baas']['base']['ss_rate'])
        return wait_loading(self)
    return True
