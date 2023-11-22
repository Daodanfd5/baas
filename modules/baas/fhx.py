from common import config
from modules.baas import restart


def start(self):
    # 重启游戏
    self.logger.info("开始反和谐BA")
    pkg = self.bc['baas']['base']['package']
    self.logger.info("开始推送反和谐文件到模拟器中")
    # 推送文件
    self.d.push(config.resource_path('assets/LocalizeConfig.txt'), '/sdcard/Android/data/{0}/files/'.format(pkg))
    self.logger.info("反和谐已完成，开始重启游戏")
    restart.start(self)
