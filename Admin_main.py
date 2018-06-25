# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Add_Doctor import Ui_Add_Doctor
# from untitled import Ui_Breast_Cancer_prediction_tool
from z import Ui_Breast_Cancer_prediction_tool


class Ui_admin_main(object):
    def setupUi(self, admin_main):
        # admin_main.setObjectName("admin_main")
        # admin_main.resize(536, 219)
        # self.centralwidget = QtWidgets.QWidget(admin_main)
        # self.centralwidget.setObjectName("centralwidget")
        # self.btn_add_doctor = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_add_doctor.setGeometry(QtCore.QRect(60, 70, 91, 41))
        # self.btn_add_doctor.setObjectName("btn_add_doctor")
        # self.btn_add_doctor.clicked.connect(self.openwindowdoctor)
        # self.btn_cancer = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_cancer.setGeometry(QtCore.QRect(260, 70, 111, 41))
        # self.btn_cancer.setObjectName("btn_cancer")
        # self.btn_cancer.clicked.connect(self.openwindowCancer)
        # admin_main.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(admin_main)
        # self.statusbar.setObjectName("statusbar")
        # admin_main.setStatusBar(self.statusbar)

        # self.retranslateUi(admin_main)
        # QtCore.QMetaObject.connectSlotsByName(admin_main)

    
        admin_main.setObjectName("admin_main")
        admin_main.resize(536, 219)
        self.centralwidget = QtWidgets.QWidget(admin_main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_doctor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_doctor.setGeometry(QtCore.QRect(60, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_doctor.setFont(font)
        self.btn_add_doctor.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 239);")
        self.btn_add_doctor.setObjectName("btn_add_doctor")
        self.btn_add_doctor.clicked.connect(self.openwindowdoctor)
        self.btn_cancer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancer.setGeometry(QtCore.QRect(260, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancer.setFont(font)
        self.btn_cancer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 218, 0);")
        self.btn_cancer.setObjectName("btn_cancer")
        self.btn_cancer.clicked.connect(self.openwindowCancer)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 180, 291, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        admin_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(admin_main)
        self.statusbar.setObjectName("statusbar")
        admin_main.setStatusBar(self.statusbar)

        self.retranslateUi(admin_main)
        QtCore.QMetaObject.connectSlotsByName(admin_main)








    def retranslateUi(self, admin_main):
        _translate = QtCore.QCoreApplication.translate
        admin_main.setWindowTitle(_translate("admin_main", "Admin_Main"))
        self.btn_add_doctor.setText(_translate("admin_main", "Add_Doctor"))
        self.btn_cancer.setText(_translate("admin_main", " Cancer prediction "))

    def openwindowdoctor(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Add_Doctor()
            self.window.hide()
            self.ui.setupUi(self.window)
            self.window.show()

    def openwindowCancer(self):
            self.window = QtWidgets.QMainWindow()
            # admin_main.hide()
            self.ui = Ui_Breast_Cancer_prediction_tool()
            self.ui.setupUi(self.window)
            self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_main = QtWidgets.QMainWindow()
    ui = Ui_admin_main()
    ui.setupUi(admin_main)
    admin_main.show()
    sys.exit(app.exec_())

