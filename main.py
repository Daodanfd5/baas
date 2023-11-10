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
    app = Flask(__name__, static_folder='web/static', static_url_path='/static')
    app.register_blueprint(baas)
    app.register_blueprint(configs)
    threading.Timer(2, open_browser).start()
    app.run(debug=False, port=1117, host='0.0.0.0')
