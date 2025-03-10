import json
import time
import unittest
import uiautomator2 as u2
from cnocr import CnOcr
from common import image, config, position, stage, ocr, log, color
from modules.scan import normal_task, main_story


class TestPosition(unittest.TestCase):

    def load_config(self):
        filepath = config.config_filepath(self.con)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.bc = data
        pass

    def setUp(self) -> None:
        self.con = 'wz'
        self.load_config()
        self.logger = log.create_logger(self.con, False)
        self.d = u2.connect(self.bc['baas']['base']['serial'])
        self.ocr = CnOcr()
        self.ocrEN = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
        self.ocrNum = CnOcr(det_model_name='number-densenet_lite_136-fc', rec_model_name='number-densenet_lite_136-fc')
        self.file_path = "../assets/images"
        position.init_assets_data(self, self.file_path)

    def click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.click(x, y)

    def click_condition(self, x, y, cond, fn, fn_args, wait=True, rate=0):
        """
        条件点击，直到不满足条件为止
        @param x: x坐标
        @param y: y坐标
        @param cond: true 或 false
        @param fn: 要执行的函数，需要返回bool
        @param fn_args: 执行函数的参数
        @param wait: 是否需要等待加载
        @param rate: 每次点击等待时间
        """
        if wait:
            stage.wait_loading(self)
        self.click(x, y, False)
        while cond != fn(self, *fn_args):
            time.sleep(rate)
            self.d.click(x, y)

    def double_click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("double_click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.double_click(x, y)

    def test_task(self):
        print(ocr.screenshot_get_text(self, (189, 197, 228, 225), self.ocrNum))
        # assert color.check_rgb_similar(self, (124, 429, 125, 430), (75, 233, 246))

    def ss_task_lv(self, base, lv, region):
        d = "{0}/{1}".format(self.file_path, base)
        f = "../assets/images/{0}/{1}-{2}.png".format(base, region, lv)
        image.screenshot_cut(self, (191, 199, 265, 224), 0, False, d, f)
        self.click(1167, 355)
        time.sleep(3)

    def test_gen_normal_task(self):
        base = 'normal_task'
        for region in range(6, 16):
            for lv in range(1, 6):
                self.ss_task_lv(base, lv, region)

    def test_gen_hard_task(self):
        base = 'hard_task'
        for region in range(6, 16):
            for lv in range(1, 4):
                self.ss_task_lv(base, lv, region)

    def test_ss(self):
        assets = [
            # 'home_cafe',
            # 'home_bus',

            # 'restart_menu',
            # 'restart_maintain',
            # 'restart_update',

            # 'arena_id',
            # 'arena_cd',
            # 'arena_0-5',
            # 'arena_skip',
            'arena_attack',

            # 'cafe_0.0',
            # 'cafe_menu',

            # 'tutor_dept_entry',
            # 'tutor_dept_title',

            # 'group_menu',

            # 'mailbox_menu',

            # 'momo_talk_no-chat',
            # 'momo_talk_sort-field',
            # 'momo_talk_sort-direction',

            # 'work_task_menu',

            # 'shop_menu',
            # 'shop_buy3',
            # 'shop_buy2',
            # 'shop_buy1',
            # 'shop_confirm',

            # 'schedule_menu',
            # 'normal_task_menu',
            # 'normal_task_task-info',
            # 'normal_task_fight-task',
            # 'normal_task_force-edit',
            # 'normal_task_fight-skip',
            # 'normal_task_auto-over',
            # 'normal_task_force-4',
            # 'normal_task_force-3',
            # 'normal_task_force-2',
            # 'normal_task_force-1',
            # 'normal_task_task-scan',
            # 'normal_task_15-1',
            # 'normal_task_15-2',
            # 'normal_task_15-3',
            # 'normal_task_15-4',
            # 'normal_task_15-5',
            # 'normal_task_side-quest',
            # 'normal_task_attack',
            # 'normal_task_prize-confirm',
            # 'normal_task_no-pass',
            # 'normal_task_move-force-confirm',
            # 'normal_task_task-finish',
            # 'normal_task_fight-task-info',

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

            # 'main_story_menu',
            # 'main_story_story',
            # 'main_story_choose-plot',
            # 'main_story_clearance',
            # 'main_story_current-clearance',
            # 'main_story_plot-info',
            # 'main_story_skip-menu',
            # 'main_story_first-lock',
            # 'main_story_plot-fight',
            # 'main_story_plot-attack',
            # 'main_story_fight-parse',
            # 'main_story_fight-confirm',
            # 'main_story_auto',
            # 'main_story_three-times',
            # 'cm_confirm'
        ]
        for asset in assets:
            base, file = asset.rsplit('_', 1)
            d = "{0}/{1}".format(self.file_path, base)
            f = "../assets/images/{0}/{1}.png".format(base, file)
            image.screenshot_cut(self, image.get_box(asset), 0, False, d, f)
        assert True
