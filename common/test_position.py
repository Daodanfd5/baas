import json
import unittest
import uiautomator2 as u2
from cnocr import CnOcr
from common import image


class TestPosition(unittest.TestCase):

    def load_config(self):
        with open('../configs/baas.json', 'r', encoding='utf-8') as f:
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

    def test_ss(self):
        assets = [
            # 'home_cafe',

            # 'restart_menu',
            # 'restart_maintain',

            # 'arena_id',
            # 'arena_cd',
            # 'arena_0-5',

            # 'cafe_0.0',

            # 'tutor_dept_entry',
            'tutor_dept_title',
        ]
        for asset in assets:
            base, file = asset.split('_', 1)
            d = "{0}/{1}".format(self.file_path, base)
            f = "../assets/{0}/{1}.png".format(base, file)
            image.screenshot_cut(self, image.get_box(asset), 0, False, d, f)
