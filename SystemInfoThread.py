import psutil
import time
from PyQt5.QtCore import QThread


class SystemInfoThread(QThread):

    def __init__(self, window):
        super(SystemInfoThread, self).__init__()
        self.__win = window

    def run(self):
        old_net_speed = psutil.net_io_counters().bytes_recv
        while True:
            new_net_speed = psutil.net_io_counters().bytes_recv
            time.sleep(1)
            self.__win.net_label.setText("%.2fK/s" % ((new_net_speed - old_net_speed) / 1024))
            self.__win.mem_label.setText(
                str(int(psutil.virtual_memory().used * 100 / psutil.virtual_memory().total)) + '%')
            old_net_speed = new_net_speed
