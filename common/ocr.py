import os
import time
from fuzzywuzzy import fuzz
from common import stage, image
from common.iconst import *


def screenshot(self):
    self.d.screenshot(SS_FILE)


def screenshot_get_text(self, area, ocr=None, wait=99999, i=0):
    # 检查文字前，等待加载完成
    stage.wait_loading(self)
    if not os.path.exists(SS_PATH):
        os.makedirs(SS_PATH)
    img = self.d.screenshot().crop(area)
    img.save(SS_FILE)
    if ocr is None:
        out = self.ocr.ocr(SS_FILE)
    else:
        out = ocr.ocr(SS_FILE)
    if len(out) == 0 and wait > 0:
        return screenshot_get_text(self, area, ocr, wait)
    if len(out) == 0:
        return ''
    return out[i]['text']


def screenshot_cut_get_text(self, area, before_wait=0, need_loading=True):
    image.screenshot_cut(self, area, before_wait, need_loading)
    return self.ocr.ocr(SS_FILE)


def screenshot_check_text(self, text, area=(), wait=99999, before_wait=0, need_loading=True):
    out = screenshot_cut_get_text(self, area, before_wait, need_loading)
    ex = any(map(lambda d: fuzz.ratio(d.get('text'), text) > 60, out))
    print("判断是否 为", text, "结果", ex)
    print("\t\t\t", out)
    # 如果已经找到 或 不需要等待直接返回结果
    if ex or wait == 0:
        return ex
    time.sleep(self.bc['baas']['ss_rate'])
    if wait < 99999:
        wait -= 1
    return screenshot_check_text(self, text, area, wait)


def screenshot_get_position(self, text, area=(), wait=99999, before_wait=0, need_loading=True):
    out = screenshot_cut_get_text(self, area, before_wait, need_loading)
    print("\t\t\t", out)
    for t in out:
        if fuzz.ratio(t.get('text'), text) <= 60:
            continue
        print("判断是否 为", text, "结果", True)
        return True, t.get('position')
    print("判断是否 为", text, "结果", False)
    # 不需要等待直接返回结果
    if wait == 0:
        return False, ()
    time.sleep(self.bc['baas']['ss_rate'])
    if wait < 99999:
        wait -= 1
    return screenshot_get_position(self, text, area, wait)
