from PyQt5 import QtCore, QtGui
import os
from urllib.request import urlretrieve
import requests
import re

class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)
    url_list_count = QtCore.pyqtSignal(int)
    url_lists = QtCore.pyqtSignal(list)

class DownMovies:

    def __init__(self, url=None):
        self.url = url

    def get_urls(self):
        # requests.packages.urllib3.disable_warnings()  # 禁用安全请求警告
        html = requests.get(url=self.url)
        html.encoding = 'utf-8'
        r = re.findall(r'#EXT-X-MEDIA-SEQUENCE:0(.*?)#EXT-X-ENDLIST', html.text, re.I | re.S)
        get_url_ts = r[0].split('\n')
        url_lists = get_url_ts[2::2]
        return url_lists

class BigWorkThread(QtCore.QThread):
    # download_proess_signal = QtCore.pyqtSignal(list)
    # 构造函数里增加形参
    def __init__(self, url=None):
        super(BigWorkThread, self).__init__()
        # 储存参数
        self.url = None
        # self.path = None
        # self.worker = None
        self.signals = WorkerSignals()
        self.down = DownMovies()

    # 重写 run() 函数，在里面干大事。
    def run(self):
        self.down.url = self.url
        url_lists = self.down.get_urls()
        self.signals.url_lists.emit(url_lists)
        # self.download_proess_signal.emit(url_lists)

class Worker(QtCore.QRunnable):

    def __init__(self, url=None, path=None):
        super(Worker, self).__init__()
        self.url = url
        self.path = path
        self.signals = WorkerSignals()

    def run(self):
        filename = os.path.basename(self.url)
        target = os.path.join(self.path, filename)
        # 判断文件是否存在，如果不存在则下载
        if not os.path.isfile(target):
            urlretrieve(self.url, self.path + "/" + filename)
            print(filename)
        else:
            print(filename + " 已存在")
        self.signals.progress.emit(1)  # Done
