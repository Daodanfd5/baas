import numpy as np
import cv2
import aircv as ac
import os
import time
from common import stage, position
from common.iconst import *


def screenshot_cut(self, area, before_wait=0, need_loading=True, path=SS_PATH, file=SS_FILE):
    """
    截图并裁剪图片
    @param self:
    @param area: 剪切区域
    @param before_wait: 前置等待时间
    @param need_loading: 等待加载
    @param path: 文件保存目录
    @param file: 文件保存完整路径
    @return: 图片对象
    """
    if before_wait > 0:
        time.sleep(before_wait)
    # 检查文字前，等待加载完成
    if need_loading:
        stage.wait_loading(self)
    # 创建目录
    if not os.path.exists(path):
        os.makedirs(path)
    if len(area) == 0:
        return self.d.screenshot(file)
    else:
        ss = self.d.screenshot()
        img = ss.crop(area)
        img.save(file)
        return img


def compare_image(self, name, retry=0, threshold=10):
    """
    对图片坐标内的图片和资源图片是否匹配
    @param self:
    @param name: 资源名称
    @param retry: 重试次数 
    @param threshold: 匹配程度0为完全匹配
    @return: 是否匹配
    """
    box = get_box(name)
    screenshot_cut(self, box, 0, False)
    ss_img = ac.imread(SS_FILE)
    res_img = position.iad[name]
    # 计算差异值
    diff = cv2.absdiff(ss_img, res_img)
    # 计算MSE（Mean Squared Error）
    mse = np.mean(diff ** 2)
    compare = mse <= threshold
    print("\t\t对比:{0} MSE:{1} 结果:{2}".format(name, mse, compare))
    if not compare and retry > 0:
        return compare_image(self, name, retry - 1, threshold)
    return compare


def get_box(name):
    """
    获取坐标
    @param name:资源名称
    @return: 坐标
    """
    module, name = name.rsplit("_", 1)
    return position.ibd[module][name]
