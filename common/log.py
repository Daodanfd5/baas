import logging
import os
import sys
from datetime import datetime


class ColoredHTMLFormatter(logging.Formatter):
    """
    Formatter that adds HTML color tags depending on the log level.
    """
    COLORS = {
        'DEBUG': 'blue',
        'INFO': 'green',
        'WARNING': 'orange',
        'ERROR': 'red',
        'CRITICAL': 'purple'
    }

    DATE_COLOR = 'blue'

    def format(self, record):
        level_color = self.COLORS.get(record.levelname, 'black')
        record.asctime = self.formatTime(record, "%H:%M:%S")
        record.levelname = f'<span style="color: {level_color};">{record.levelname}</span>'
        message = super().format(record)
        return message.replace('\n', '<br />')

    # Override formatTime to use our custom date format
    def formatTime(self, record, datefmt=None):
        datefmt = "%m-%d %H:%M:%S"
        ct = datetime.fromtimestamp(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            try:
                s = ct.isoformat(timespec='milliseconds')
            except TypeError:
                s = ct.isoformat()
        return s


class StreamToLogger:
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())

    def flush(self):
        pass


def create_logger(con):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        log_dir_path = './runtime/logs'
        if not os.path.exists(log_dir_path):
            os.makedirs(log_dir_path)
            print(f"The directory {log_dir_path} was created.")
        current_date = datetime.now().strftime('%Y-%m-%d')
        file_handler = logging.FileHandler(f'./runtime/logs/{current_date}_{con}.log', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = ColoredHTMLFormatter(
            '<p>%(levelname)s\t<span style="color:#0598bc">%(asctime)s</span> │ <span style="color:#616161">%(message)s</span></p>')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        stdout_logger_handler = StreamToLogger(logger, logging.INFO)
        stderr_logger_handler = StreamToLogger(logger, logging.ERROR)

        sys.stdout = stdout_logger_handler
        sys.stderr = stderr_logger_handler

    return logger
