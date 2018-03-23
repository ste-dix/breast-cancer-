# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Doctor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys

class Ui_Add_Doctor(object):
    def setupUi(self, Add_Doctor):
        Add_Doctor.setObjectName("Add_Doctor")
        Add_Doctor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Add_Doctor)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 170, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 170, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 250, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 290, 71, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 210, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 250, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 290, 201, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(320, 390, 75, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.adddoctor)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 60, 231, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 330, 201, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 330, 71, 21))
        self.label_6.setObjectName("label_6")
        Add_Doctor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Add_Doctor)
        self.statusbar.setObjectName("statusbar")
        Add_Doctor.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Doctor)
        QtCore.QMetaObject.connectSlotsByName(Add_Doctor)

    def retranslateUi(self, Add_Doctor):
        _translate = QtCore.QCoreApplication.translate
        Add_Doctor.setWindowTitle(_translate("Add_Doctor", "MainWindow"))
        self.label.setText(_translate("Add_Doctor", "Doctor\'s Name"))
        self.label_2.setText(_translate("Add_Doctor", "Phone Number"))
        self.label_3.setText(_translate("Add_Doctor", "Designation"))
        self.label_4.setText(_translate("Add_Doctor", "Address"))
        self.btn_add.setText(_translate("Add_Doctor", "Add Doctor"))
        self.label_5.setText(_translate("Add_Doctor", "ADD DOCTOR"))
        self.label_6.setText(_translate("Add_Doctor", "Password"))



    def adddoctor(self):
        username = self.lineEdit.text()
        Designation1 =self.lineEdit_2.text()
        phone1 = self.lineEdit_3.text()
        address1 =self.lineEdit_4.text()
        password1 =self.lineEdit_5.text()



        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR,db_file,"JMJ.db")
        connection = sqlite3.connect(db_path)


        with connection:
            cur =connection.cursor()
            cur.execute(" INSERT INTO J(name,designation	,phone,address,password)"
                         "VALUES('%s','%s' ,'%s','%s','%s')" %(''.join(username),
                         ''.join(Designation1),
                         ''.join(phone1),
                         ''.join(address1),
                        ''.join(password1))
            
            
            )
	
	
	
	

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Doctor = QtWidgets.QMainWindow()
    ui = Ui_Add_Doctor()
    ui.setupUi(Add_Doctor)
    Add_Doctor.show()
    sys.exit(app.exec_())

