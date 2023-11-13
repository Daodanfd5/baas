import logging
import sys
from datetime import datetime


class StreamToLogger:
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        # Avoid writing empty messages or just newlines etc
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())

    def flush(self):
        # This flush method is needed for stream compatibility
        pass


def create_logger(con):
    # 创建logger对象。如果不指定name，那么将会返回root logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG

    # 防止重复添加handler
    if not logger.handlers:
        # 创建一个handler，用于写入日志文件
        current_date = datetime.now().strftime('%Y-%m-%d')
        file_handler = logging.FileHandler(f'./runtime/{current_date}_{con}.log')
        file_handler.setLevel(logging.DEBUG)  # 设置handler的日志级别

        # 创建一个formatter，设置日志格式
        formatter = logging.Formatter('%(levelname)s     %(asctime)s │ %(message)s')
        file_handler.setFormatter(formatter)

        # 将file handler添加到logger对象中
        logger.addHandler(file_handler)

        # 创建stdout和stderr日志重定向对象
        stdout_logger_handler = StreamToLogger(logger, logging.INFO)
        stderr_logger_handler = StreamToLogger(logger, logging.ERROR)

        # 重定向stdout和stderr到日志系统
        sys.stdout = stdout_logger_handler
        sys.stderr = stderr_logger_handler

    return logger
