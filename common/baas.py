import json
import sys
import time
import uiautomator2 as u2
from uiautomator2 import Device
from datetime import datetime, timedelta
from cnocr import CnOcr

from common import stage, process, config, log
from modules.activity import tutor_dept
from modules.baas import restart
from modules.daily import group, shop, cafe, schedule, special_entrust, wanted, arena, make, buy_ap
from modules.reward import momo_talk, work_task, mailbox
from modules.scan import normal_task, hard_task

func_dict = {
    'group': group.start,
    'momo_talk': momo_talk.start,
    'shop': shop.start,
    'cafe': cafe.start,
    'schedule': schedule.start,
    'special_entrust': special_entrust.start,
    'wanted': wanted.start,
    'arena': arena.start,
    'make': make.start,
    'work_task': work_task.start,
    'normal_task': normal_task.start,
    'hard_task': hard_task.start,
    'mailbox': mailbox.start,
    'restart': restart.start,

    'tutor_dept': tutor_dept.start,
    'buy_ap': buy_ap.start,
}


class Baas:
    ocr: CnOcr
    ocrEN: CnOcr
    ocrNum: CnOcr
    d: Device
    bc: dict  # baas config BA配置
    tc: dict  # task config 任务配置

    def __init__(self, con, processes_task):
        self.con = con
        if processes_task is None:
            return
        self.load_config()
        self.d = u2.connect(self.bc['baas']['serial'])
        self.ocr = CnOcr()
        self.ocrEN = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
        self.ocrNum = CnOcr(det_model_name='number-densenet_lite_136-fc', rec_model_name='number-densenet_lite_136-fc')
        self.processes_task = processes_task
        self.logger = log.create_logger(con)
        self.check_resolution()

    def check_resolution(self):
        # 1280 * 720
        if self.d.info['displayWidth'] != 1280 or self.d.info['displayHeight'] != 720:
            self.logger.critical("分辨率必须为 1280 * 720")
            sys.exit(1)
            

    def log_title(self, msg):
        pre = 'Scheduler: Start task `{0}`</br>'.format(msg)
        s = '<span style="color: #14ce14; text-decoration-color: #14ce14">═════════════════════════════════════════════════════════════════════════════════════════════════</span>'
        self.logger.info(pre + s + "</br><div style='color:#42A5F5;width:800px;' align='center'>" + msg + "</div>" + s)

    def click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.click(x, y)

    def click_condition(self, x, y, cond, fn, fn_args, wait=True, rate=0):
        """
        条件点击，直到不满足条件为止
        @param x: x坐标
        @param y: y坐标
        @param cond: true 或 false 
        @param fn: 要执行的函数，需要返回bool
        @param fn_args: 执行函数的参数
        @param wait: 是否需要等待加载
        @param rate: 每次点击等待时间
        """
        if wait:
            stage.wait_loading(self)
        self.click(x, y, False)
        while cond != fn(self, *fn_args):
            time.sleep(rate)
            self.click(x, y, False)

    def double_click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("double_click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.double_click(x, y)

    def swipe(self, fx, fy, tx, ty):
        self.logger.info("swipe %s %s %s %s", fx, fy, tx, ty)
        self.d.swipe(fx, fy, tx, ty)

    def dashboard(self):
        # 使用字典将字符串映射到对应的函数
        self.log_title("BA启动")
        no_task = False
        while True:
            fn, tc = self.get_task()
            if fn is None:
                if not no_task:
                    self.logger.info("All tasks have been executed.")
                no_task = True
                time.sleep(3)
                continue
            no_task = False
            # 从字典中获取函数并执行
            if fn in func_dict:
                self.processes_task[self.con] = fn
                self.tc = tc
                self.tc['task'] = fn
                self.finish_seconds = 0
                self.log_title("开始执行【" + tc['text'] + "】")
                func_dict[fn](self)
                self.finish_task(fn)
                self.log_title("执行完成【" + tc['text'] + "】")
                del self.processes_task[self.con]
            else:
                self.logger.info(f"函数不存在:{fn}")
                sys.exit(0)

    def config_path(self):
        return config.config_filepath(self.con)

    def load_config(self):
        with open(self.config_path(), 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.bc = data
        pass

    def save_config(self):
        with open(self.config_path(), 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.bc, indent=4, ensure_ascii=False))

    def get_task(self):
        self.load_config()
        queue = []
        for ba_task, con in self.bc.items():
            if ba_task == 'baas':
                continue
            # 超出截止时间
            if not con['enable'] or datetime.strptime(con['end'], "%Y-%m-%d %H:%M:%S") < datetime.now():
                continue
            # 时间未到
            if datetime.strptime(con['next'], "%Y-%m-%d %H:%M:%S") > datetime.now():
                continue
            task = {'index': con['index'], 'next': con['next'], 'task': ba_task, 'con': con}
            queue.append(task)
        queue.sort(key=lambda x: (x['index'], datetime.strptime(x['next'], "%Y-%m-%d %H:%M:%S")))
        if len(queue) > 0:
            return queue[0]['task'], queue[0]['con']
        return None, None

    def task_schedule(self, run_task):
        self.load_config()
        running = []
        waiting = []
        queue = []
        closed = []
        for ba_task, con in self.bc.items():
            # 被关闭的功能
            if ba_task == 'baas':
                continue
            task = {'next': con['next'], 'task': ba_task, 'text': con['text'], 'index': con['index']}
            # 正在运行中的任务
            if run_task is not None and run_task == ba_task:
                running.append(task)
                continue
            if not con['enable'] or datetime.strptime(con['end'], "%Y-%m-%d %H:%M:%S") < datetime.now():
                closed.append(task)
                continue
            # 时间未到
            if datetime.strptime(con['next'], "%Y-%m-%d %H:%M:%S") > datetime.now():
                waiting.append(task)
                continue
            # 队列中
            queue.append(task)

        waiting.sort(key=lambda x: (x['index'], datetime.strptime(x['next'], "%Y-%m-%d %H:%M:%S")))
        queue.sort(key=lambda x: (x['index'], datetime.strptime(x['next'], "%Y-%m-%d %H:%M:%S")))
        return {'running': running, 'waiting': waiting, 'queue': queue, 'closed': closed,
                'run_state': process.m.state_process(self.con)}

    def find_exec_task(self):
        """
        查找关联任务立刻执行
        """
        if 'link_task' in self.tc:
            self.finish_seconds = 1
            task = self.tc['link_task']
            self.tc = self.bc[task]
            self.finish_task(task)

    def finish_task(self, fn):
        self.load_config()
        # 获取当前日期时间
        now = datetime.now()
        if self.finish_seconds > 0:
            future = now + timedelta(seconds=self.finish_seconds)
        else:
            # 计算下次执行时间
            if 'interval' in self.tc:
                future = now + timedelta(seconds=self.tc['interval'])
            else:
                future = now + timedelta(days=1)
                # 别问我为什么要写5点 :)
                future = datetime(future.year, future.month, future.day, 5, 0)
        # 将datetime对象转成字符串
        self.bc[fn]['next'] = future.strftime("%Y-%m-%d %H:%M:%S")
        # 完成任务
        if 'task' in self.tc:
            del self.tc["task"]
        self.save_config()
        # 查找关联任务立刻执行
        self.find_exec_task()
