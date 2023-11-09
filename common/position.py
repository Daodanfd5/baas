import os
import aircv as ac

from modules.baas import home

# 图片资源数据 image assets data
from modules.daily import arena, cafe

iad = {
}
# 图片坐标数据 image box data
ibd = {
    'home': home.x,
    'arena': arena.x,
    'cafe': cafe.x
}


def init_assets_data():
    """
    初始化资源文件数据
    """
    assets_dir = 'assets'
    for dp, dns, fns in os.walk(assets_dir):
        for fn in fns:
            if not fn.endswith('.png'):
                continue
            filepath = os.path.join(dp, fn)
            key = os.path.relpath(filepath, assets_dir)  # 获取文件在assets目录下的相对路径作为键
            key = os.path.splitext(key)[0].replace('/', '_')  # 去除文件扩展名
            iad[key] = ac.imread(filepath)
