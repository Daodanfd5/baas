import logging
from datetime import datetime


def create_logger():
    # 创建logger对象。如果不指定name，那么将会返回root logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG
    # 创建一个handler，用于写入日志文件
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_handler = logging.FileHandler(f'./runtime/{current_date}_kc.log')
    file_handler.setLevel(logging.DEBUG)  # 设置handler的日志级别
    # 创建一个formatter，设置日志格式
    formatter = logging.Formatter('%(levelname)s     %(asctime)s │ %(message)s')
    file_handler.setFormatter(formatter)
    # 将handler添加到logger对象中
    logger.addHandler(file_handler)
    return logger
