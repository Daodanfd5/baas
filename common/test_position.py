import json
import time
import unittest
import uiautomator2 as u2
from cnocr import CnOcr
from common import image, config, position, stage, ocr
from modules.daily import group
from modules.scan import normal_task


class TestPosition(unittest.TestCase):

    def load_config(self):
        filepath = config.config_filepath('baas')
        with open("." + filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.bc = data
        pass

    def setUp(self) -> None:
        self.load_config()
        self.d = u2.connect(self.bc['baas']['serial'])
        self.ocr = CnOcr()
        self.ocrEN = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
        self.ocrNum = CnOcr(det_model_name='number-densenet_lite_136-fc', rec_model_name='number-densenet_lite_136-fc')
        self.file_path = "../assets"
        position.init_assets_data(self.file_path)

    def click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            print("\t\t\n\n Click", x, y, "\n\n")
            if rate > 0:
                time.sleep(rate)
            self.d.click(x, y)

    def double_click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            print("\t\t\n\n DoubleClick", x, y, "\n\n")
            if rate > 0:
                time.sleep(rate)
            self.d.double_click(x, y)

    def test_task(self):
        print(image.compare_image(self, 'shop_buy3'))
        # ocr.screenshot_check_text(self, '', (610, 146, 640, 175), 0)
        # self.tc = {}
        # self.tc['task'] = 'normal_task'
        # normal_task.start(self)

    def test_ss(self):
        assets = [
            # 'home_cafe',
            # 'home_bus',

            # 'restart_menu',
            # 'restart_maintain',

            # 'arena_id',
            # 'arena_cd',
            # 'arena_0-5',
            # 'arena_skip',

            # 'cafe_0.0',
            # 'cafe_menu',

            # 'tutor_dept_entry',
            # 'tutor_dept_title',

            # 'group_menu',

            # 'mailbox_menu',

            # 'momo_talk_no-chat',
            # 'momo_talk_sort-field',
            'momo_talk_sort-direction',

            # 'work_task_menu',

            # 'shop_menu',
            # 'shop_buy3',
            # 'shop_buy2',
            # 'shop_buy1',
            # 'shop_confirm',

            # 'schedule_menu',
            # 'normal_task_menu',

            # 'buy_ap_notice',
            # 'buy_ap_notice2',
            # 'buy_ap_limited',
            # 'buy_ap_buy20',
            # 'buy_ap_buy19',
            # 'buy_ap_buy18',
            # 'buy_ap_buy17',
            # 'buy_ap_buy16',
            # 'buy_ap_buy15',
            # 'buy_ap_buy14',
            # 'buy_ap_buy13',
            # 'buy_ap_buy12',
            # 'buy_ap_buy11',
            # 'buy_ap_buy10',
            # 'buy_ap_buy9',
            # 'buy_ap_buy8',
            # 'buy_ap_buy7',
            # 'buy_ap_buy6',
            # 'buy_ap_buy5',
            # 'buy_ap_buy4',
            # 'buy_ap_buy3',
            # 'buy_ap_buy2',
            # 'buy_ap_buy1',
        ]
        for asset in assets:
            base, file = asset.rsplit('_', 1)
            d = "{0}/{1}".format(self.file_path, base)
            f = "../assets/{0}/{1}.png".format(base, file)
            image.screenshot_cut(self, image.get_box(asset), 0, False, d, f)
