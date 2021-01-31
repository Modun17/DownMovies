from DownMovieGui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QFont, QPalette
from SystemInfoThread import SystemInfoThread
from threads_one import Worker, BigWorkThread
import re
import requests

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        # 控制显示实时网速和内存使用信息
        sys_info_thread = SystemInfoThread(self.ui)
        sys_info_thread.start()

        self.ui.setupUi(self)

        self.ui.button_add.clicked.connect(self.get_url)
        self.ui.button_submit.clicked.connect(self.query_formula)
        self.ui.button_reset.clicked.connect(self.reset)
        self.ui.button_path_file.clicked.connect(self.setFilePath)
        self.ui.button_submit.setEnabled(False)

        self.ui.actionQuit.setShortcut('Ctrl+Q')
        self.ui.actionQuit.setStatusTip('Exit application')
        self.ui.actionQuit.triggered.connect(qApp.quit)

        self.step = 0
        self.count = 0
        self.worker = None
        self.url_list = []
        self.url_lists = []
        self.setLabel()

    def get_url(self):
        self.ui.button_add.setEnabled(False)
        self.big = BigWorkThread()
        self.big.url = self.ui.lineEdit_url.text()
        self.big.signals.url_lists.connect(self.look_if)
        self.big.start()

    def query_formula(self):
        """
        获取输入并且把输入的网址和存储路径赋值给下载文件
        :return:
        """
        if self.url_lists and self.ui.lineEdit_path.text():
            self.reset()

            thread_pool = QtCore.QThreadPool.globalInstance()
            for index, task in enumerate(self.url_lists):
                url_before = re.findall(r'(.*?)index.m3u8', self.url_list[index])[0]
                for u in task:
                    url = url_before + u
                    self.worker = Worker(url=url, path=self.ui.lineEdit_path.text())
                    self.worker.signals.progress.connect(self.change_progressbar_value)
                    thread_pool.start(self.worker)

        elif not self.url_lists:
            self.ui.label_error_url.setText("请添加下载任务")
            self.ui.label_error_url.setStyleSheet("color:red")
            self.ui.label_error_path.setText("")
        elif not self.ui.lineEdit_path.text():
            self.ui.label_error_url.setText("")
            self.ui.label_error_path.setText("请输入保存路径")
            self.ui.label_error_path.setStyleSheet("color:red")

    def reset(self):
        """
        清空所有输入
        :return:
        """
        # self.step = 0
        # self.ui.progressBar.setValue(0)
        self.ui.button_submit.setEnabled(False)
        self.ui.label_error_path.setText("")
        self.ui.label_error_url.setText("")
        self.ui.listWidget_roll.clear()
        # self.url_list = []
        # self.url_lists = []

    def setFilePath(self):
        """
        设置打开选择存储路径
        :return:
        """
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "./")
        self.ui.lineEdit_path.setText(download_path)

    def look_if(self, value):
        self.ui.button_add.setEnabled(True)
        self.ui.button_submit.setEnabled(True)

        self.ui.listWidget_roll.addItem("准备下载 " + self.ui.lineEdit_url.text())

        self.url_list.append(self.ui.lineEdit_url.text())
        self.url_lists.append(value)

        self.count = self.count + len(value)
        print(self.url_list)
        print(self.url_lists)
        print(self.count)
        # self.ui.listWidget_roll.addItem(value)

    # 控制进度条显示
    def change_progressbar_value(self, value):
        """
        控制进度条显示
        :param value:
        :return:
        """
        self.step = self.step + value
        self.ui.progressBar.setValue(int(self.step / self.count * 100))
        if int(self.step / self.count * 100) == 100:
            QMessageBox.information(self, "提示", "下载成功！")
            self.ui.button_submit.setEnabled(True)

    def setLabel(self):
        """
        显示实时网速和内存使用
        :return:
        """
        pal = QPalette()
        pal.setColor(QPalette.WindowText, Qt.white)

        self.ui.mem_label.setMinimumWidth(60)
        self.ui.mem_label.setAlignment(Qt.AlignHCenter)
        # 设置控件背景色
        pal.setColor(QPalette.Window, Qt.green)
        self.ui.mem_label.setAutoFillBackground(True)
        self.ui.mem_label.setPalette(pal)

        # 文本居中显示
        self.ui.net_label.setAlignment(Qt.AlignHCenter)
        # 设置控件背景色
        pal.setColor(QPalette.Window, Qt.red)
        self.ui.net_label.setAutoFillBackground(True)
        self.ui.net_label.setPalette(pal)

        font = QFont("微软雅黑", 10)
        self.ui.mem_label.setFont(font)
        self.ui.net_label.setFont(font)

        self.ui.mem_label.setText("0%")
        self.ui.net_label.setText("0K/s")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())