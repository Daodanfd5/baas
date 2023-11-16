import multiprocessing
import os
from common import process
import logging
import threading

from flask import Flask
import webbrowser
from web.baas import baas
from web.configs import configs


# 使用一个子线程打开浏览器
def open_browser():
    webbrowser.open_new('http://localhost:1117/')


if __name__ == '__main__':
    main_process_pid = os.getpid()
    multiprocessing.freeze_support()

    process.manager = multiprocessing.Manager()
    process.processes_task = process.manager.dict()

    if os.getpid() == main_process_pid:
        app = Flask(__name__, static_folder='web/static', static_url_path='/static')
        app.register_blueprint(baas)
        app.register_blueprint(configs)
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        # threading.Timer(1, open_browser).start()
        app.run(debug=False, port=1118, host='0.0.0.0')
