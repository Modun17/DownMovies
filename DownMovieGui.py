# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(550, 70, 91, 31))
        self.button_submit.setObjectName("button_submit")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(80, 70, 81, 31))
        self.label_url.setObjectName("label_url")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(80, 130, 81, 31))
        self.label_path.setObjectName("label_path")
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(170, 70, 251, 31))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setGeometry(QtCore.QRect(170, 130, 251, 31))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(550, 130, 91, 31))
        self.button_reset.setObjectName("button_reset")
        self.button_path_file = QtWidgets.QPushButton(self.centralwidget)
        self.button_path_file.setGeometry(QtCore.QRect(440, 130, 91, 31))
        self.button_path_file.setObjectName("button_path_file")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 190, 471, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.net_label = QtWidgets.QLabel(self.centralwidget)
        self.net_label.setGeometry(QtCore.QRect(170, 20, 81, 41))
        self.net_label.setText("")
        self.net_label.setObjectName("net_label")
        self.mem_label = QtWidgets.QLabel(self.centralwidget)
        self.mem_label.setGeometry(QtCore.QRect(90, 20, 81, 41))
        self.mem_label.setText("")
        self.mem_label.setObjectName("mem_label")
        self.label_percent = QtWidgets.QLabel(self.centralwidget)
        self.label_percent.setGeometry(QtCore.QRect(80, 190, 81, 31))
        self.label_percent.setObjectName("label_percent")
        self.label_error_path = QtWidgets.QLabel(self.centralwidget)
        self.label_error_path.setGeometry(QtCore.QRect(170, 170, 251, 16))
        self.label_error_path.setText("")
        self.label_error_path.setObjectName("label_error_path")
        self.label_error_url = QtWidgets.QLabel(self.centralwidget)
        self.label_error_url.setGeometry(QtCore.QRect(170, 110, 251, 16))
        self.label_error_url.setText("")
        self.label_error_url.setObjectName("label_error_url")
        self.listWidget_roll = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_roll.setGeometry(QtCore.QRect(80, 260, 561, 191))
        self.listWidget_roll.setObjectName("listWidget_roll")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(440, 70, 91, 31))
        self.button_add.setObjectName("button_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindown = QtWidgets.QMenu(self.menubar)
        self.menuWindown.setObjectName("menuWindown")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindown.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频下载器m3u8"))
        self.button_submit.setText(_translate("MainWindow", "下载"))
        self.label_url.setText(_translate("MainWindow", "  网 址："))
        self.label_path.setText(_translate("MainWindow", "存储路径："))
        self.button_reset.setText(_translate("MainWindow", "清空"))
        self.button_path_file.setText(_translate("MainWindow", "选择路径"))
        self.label_percent.setText(_translate("MainWindow", "下载总进度"))
        self.button_add.setText(_translate("MainWindow", "添加"))
        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindown.setTitle(_translate("MainWindow", "windown"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        self.actionNewFile.setText(_translate("MainWindow", "new file"))
        self.actionOpenFile.setText(_translate("MainWindow", "openfile"))
        self.actionQuit.setText(_translate("MainWindow", "quit"))
