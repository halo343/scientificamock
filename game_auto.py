# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created: Mon Sep  6 10:29:22 2021
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(634, 512)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 10, 191, 341))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ln_password = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ln_password.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ln_password.setObjectName(_fromUtf8("ln_password"))
        self.verticalLayout_2.addWidget(self.ln_password)
        self.ln_guess = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ln_guess.setEnabled(False)
        self.ln_guess.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ln_guess.setObjectName(_fromUtf8("ln_guess"))
        self.verticalLayout_2.addWidget(self.ln_guess)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 350, 351, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_start = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setEnabled(True)
        self.btn_start.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_guess = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_guess.setEnabled(False)
        self.btn_guess.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_guess.setObjectName(_fromUtf8("btn_guess"))
        self.horizontalLayout.addWidget(self.btn_guess)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 100, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
        self.btn_guess.setText(_translate("MainWindow", "Guess", None))
        self.label.setText(_translate("MainWindow", "Password", None))
        self.label_2.setText(_translate("MainWindow", "Guess", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

