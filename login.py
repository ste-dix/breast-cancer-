    # -*- coding: utf-8 -*-
#jesus+mary+joseph
# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
import sqlite3
from untitled import  Ui_Breast_Cancer_prediction_tool
import os.path
import sys
from Admin_main import Ui_admin_main










# class Ui_MainWindow(object)
#     def loginCheck(self):
#         username = self.Uname.text()
#         password = self.password_2()


#         Connection =sqlite3.connect("breastCancer.db")
#         result = Connection.execute("select * from user where name = ? password = ?" ,(name ,password))
#         if(len(result.fetchall()) > 0):
#             print("user found !")

#         else:
#             print("user name not found")    


class Ui_MainWindow(object):

   

        











    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Uname = QtWidgets.QLineEdit(self.centralwidget)
        self.Uname.setGeometry(QtCore.QRect(290, 100, 161, 21))
        self.Uname.setObjectName("Uname")
        self.password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_2.setGeometry(QtCore.QRect(290, 160, 161, 20))
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setPlaceholderText("")
        self.password_2.setObjectName("password_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 100, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 160, 71, 21))
        self.label_2.setObjectName("label_2")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(300, 210, 75, 23))
        self.Login.setObjectName("Login")
        self.Login.clicked.connect(self.loginCheck)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.Login.setText(_translate("MainWindow", "Login"))



    def massagebox(self,title,message):
            msgbox = QtGui.QMessageBox()
            msgbox.setIcon(QtGui.QMessageBox.WARNING)
            msgbox.setWindowTitle(title)
            msgbox.setText(message)
            msgbox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgbox.exec_()

    def openwindow(self):
        
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Breast_Cancer_prediction_tool()
            self.ui.setupUi(self.window)
            self.window.show()

    def openwindowAdmin(self):

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_admin_main()
            self.ui.setupUi(self.window)
            self.window.show()



    def loginCheck(self):

        BASE_DIR = os.path.dirname(os.path.abspath("C:/"))
        db_file = "\sqlite"
        db_path = os.path.join(BASE_DIR,db_file,"JMJ.db")
        connection = sqlite3.connect(db_path)

        username = self.Uname.text()
        password = self.password_2.text()
        
        # if (self.Uname.text() >'1'):

        #     print("user found !")
        #     self.openwindow()

        # else:
        #     print("user name not found") 
        #     self.massagebox('warning','Enter Correct username & password')
        # connection.close()
    

        # connection = sqlite3.connect("breastCancer.db")
        cursor = connection.cursor()    
        cursor.execute("SELECT * FROM JMJ WHERE name =? AND password =?" ,(username ,password))
        result = cursor.fetchall(); 
        
        for r in result:
            des = r[3]



        if(des==2):
            print("user found !")
            self.openwindowAdmin()

        elif (des==3):
            self.openwindow()

            

        else:
            print("user name not found") 
            # self.massagebox('warning','Enter Correct username & password')
        # connection.close()
        
    


       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

