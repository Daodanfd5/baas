from multiprocessing import Process
from common import position, log, config
from common.baas import Baas


def baas_dashboard(con, pt):
    b = None
    try:
        b = Baas(con, pt)
        position.init_assets_data(b)
        b.dashboard()
    except Exception as e:
        with open(config.resource_path('runtime/logs/error.txt'), 'w') as file:
            if b is not None:
                b.logger.info("{0}".format(e))
            file.write("{0}".format(e))

        # 主进程运行中的任务


manager = None
processes_task = None


class Main:
    def __init__(self):
        self.processes = {}  # 存储所有的进程

    def start_process(self, con):
        """
        启动进程
        @param con: 配置文件名称
        """
        # 如果对应的进程没有运行，则启动它
        if con not in self.processes or not self.processes[con].is_alive():
            self.processes[con] = Process(target=baas_dashboard, args=(con, processes_task))
            self.processes[con].start()

    def stop_process(self, con):
        """
        停止进程
        @param con: 配置文件名称
        """
        if con in self.processes and self.processes[con].is_alive():
            # 请求终止baas进程
            self.processes[con].terminate()
            # 等待进程实际结束
            self.processes[con].join()
            log.create_logger(con).info("停止运行")
            if con in processes_task:
                del processes_task[con]

    def state_process(self, con):
        """
        获取进程执行状态
        @param con: 配置文件名称
        """
        if con in self.processes:
            return self.processes[con].is_alive()
        else:
            return False

    def run_task(self, con):
        """
        获取进程执行中的任务
        @param con: 配置文件名称
        """
        if con in processes_task:
            return processes_task[con]
        return None


m = Main()
