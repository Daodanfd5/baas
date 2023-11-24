import json
import os
import sys


def load_ba_config(con):
    with open(config_filepath(con), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_ba_config(con, data):
    with open(config_filepath(con), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False))


def resource_path(relative_path):
    if hasattr(sys, 'frozen'):
        # 当使用 PyInstaller 打包后
        if sys.platform == 'darwin':
            # 对于 macOS, 'sys.executable' 将指向 '.app' 中的 'MacOS' 目录内的可执行文件
            # 所以我们需要往上跳转三层目录找到 '.app' 包的根目录
            base = os.path.abspath(os.path.join(os.path.dirname(sys.executable), '..', '..', '..'))
        else:
            # 其他平台，或者其他情况下保守处理，默认与Windows相同处理
            base = os.path.dirname(sys.executable)
    else:
        # 在开发环境中，直接返回脚本所在目录
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)


def config_filepath(con):
    return '{0}/{1}.json'.format(resource_path("configs"), con)


def config_dir():
    return resource_path("configs")


def get_runtime_path():
    return resource_path("runtime")


def get_ss_path(self):
    return '{0}/ss_{1}.png'.format(resource_path("runtime"), self.con)
