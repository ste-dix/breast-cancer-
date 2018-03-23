# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from tkinter import *


class Ui_Breast_Cancer_prediction_tool(object):
    def setupUi(self, Breast_Cancer_prediction_tool):
        Breast_Cancer_prediction_tool.setObjectName("Breast_Cancer_prediction_tool")
        Breast_Cancer_prediction_tool.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Breast_Cancer_prediction_tool)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 121, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Breast_Cancer_prediction_tool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Breast_Cancer_prediction_tool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Breast_Cancer_prediction_tool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Breast_Cancer_prediction_tool)
        self.statusbar.setObjectName("statusbar")
        Breast_Cancer_prediction_tool.setStatusBar(self.statusbar)

        self.retranslateUi(Breast_Cancer_prediction_tool)
        QtCore.QMetaObject.connectSlotsByName(Breast_Cancer_prediction_tool)



        

        # root = tk()
        # root.fileName = filedialog.askopenfilename(filetypes= (("all files","*.*")))

    # def File_open(self, Breast_Cancer_prediction_tool):
    #     name =QtGui.QfileDialog.getOpenFileName(self, Breast_Cancer_prediction_tool,'Open File')
    #     file = open(name ,'r')

    #     self.editor()

    #     with file:
    #         text = file.read()
    #         self.textEdit.setText(text)


    def retranslateUi(self, Breast_Cancer_prediction_tool):
        _translate = QtCore.QCoreApplication.translate
        Breast_Cancer_prediction_tool.setWindowTitle(_translate("Breast_Cancer_prediction_tool", "MainWindow"))
        self.label.setText(_translate("Breast_Cancer_prediction_tool", "Breast Cancer Prediction"))
        self.pushButton.setText(_translate("Breast_Cancer_prediction_tool", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Breast_Cancer_prediction_tool = QtWidgets.QMainWindow()
    ui = Ui_Breast_Cancer_prediction_tool()
    ui.setupUi(Breast_Cancer_prediction_tool)
    Breast_Cancer_prediction_tool.show() 
    sys.exit(app.exec_())

