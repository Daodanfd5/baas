import math
import time

import cv2
import numpy as np

from common import ocr, config, image


def color_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


def check_rgb(self, area, rgb):
    """
    根据一个坐标判断rgb
    """
    area = (area[0], area[1], area[0] + 10, area[1] + 10)
    ocr.screenshot_check_text(self, '', area, 0)
    img = cv2.imread(config.get_ss_path(self))
    return np.array_equal(img[0][0], np.array(rgb))


def wait_rgb_similar(self, area, rgb, retry=999, threshold=20, rate=0.1):
    """
    等待相似颜色出现
    """
    compare = check_rgb_similar(self, area, rgb)
    if not compare and retry > 0:
        time.sleep(rate)
        return wait_rgb_similar(self, area, rgb, retry - 1, threshold)
    return compare


def check_rgb_similar(self, area=(1090, 683, 1091, 684), rgb=(75, 238, 249), threshold=20):
    """
    判断颜色是否相近，用来判断按钮是否可以点击
    """
    image.screenshot_cut(self, area, need_loading=False)
    img = cv2.imread(config.get_ss_path(self))
    dist = color_distance(img[0][0], rgb)
    result = dist <= threshold
    self.logger.info("check_rgb_similar area:%s target_rgb:%s get_rgb:%s color_dist: %s result:%s", area, rgb,
                     img[0][0], dist, result)
    return result
