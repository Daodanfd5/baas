import time

from common import config


def start(self):
    # 重启游戏
    self.logger.info("开始反和谐BA")
    pkg = self.bc['baas']['base']['package']
    self.d.app_stop(pkg)
    self.d.app_start(pkg)
    time.sleep(5)
    self.logger.info("开始推送反和谐文件到模拟器中")
    # 推送文件
    self.d.push(config.resource_path('assets/LocalizeConfig.txt'), '/Android/data/{0}/files/'.format(pkg))
    self.logger.info("反和谐已完成，开始重启游戏")
    self.d.app_stop(pkg)
    self.d.app_start(pkg)
