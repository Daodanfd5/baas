import datetime
import os
import traceback

from common import process
from common.baas import Baas
from flask import Blueprint, render_template, send_from_directory

baas = Blueprint('baas', __name__, template_folder='templates')


@baas.route('/static/<path:path>')
def send_file(path):
    return send_from_directory(baas.static_folder, path)


@baas.route("/")
def homepage():
    return render_template('index.html')


@baas.route('/baas/start/<string:con>')
def start_baas(con):
    process.m.start_process(con)
    return {'data': {}, 'code': 200}, 200


@baas.route('/baas/stop/<string:con>')
def stop_baas(con):
    process.m.stop_process(con)
    return {'data': {}, 'code': 200}, 200


@baas.route('/baas/state/<string:con>')
def state_baas(con):
    return {'data': {'state': process.m.state_process(con)}, 'code': 200}, 200


@baas.route('/baas/schedule/<string:con>')
def schedule(con):
    running = process.m.state_process(con)
    return {'data': Baas(con).task_schedule(running), 'code': 200}, 200


@baas.route('/baas/logs/<string:con>/<int:index>')
def logs(con, index):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    fn = os.path.join('runtime', '{}_{}.txt'.format(date, con))
    if not os.path.exists(fn):
        return {'data': {'logs': '', 'index': 0}, 'code': 200}, 200
    # 读取日志
    with open(fn, 'r') as file:
        if index == 0:
            file.seek(0, os.SEEK_END)
            index = max(file.tell() - 1024 * 100, 0)
        file.seek(index)
        datas = file.read()
        new_index = file.tell()
    return {'data': {'logs': datas, 'index': new_index}, 'code': 200}, 200


# 处理所有Exception类型的错误
@baas.errorhandler(Exception)
def handle_exception(e):
    full_traceback_info = traceback.format_exc()
    return {'msg': full_traceback_info, 'code': 500}, 500
