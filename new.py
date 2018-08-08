# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from keras.preprocessing.image import ImageDataGenerator
from PyQt5.QtGui import *
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.callbacks import TensorBoard
from keras.utils import plot_model
import tensorflow as tf
import keras
import json
import time
import sys
import os
import numpy
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import glob
import cv2















class Ui_Breast_Cancer_prediction_tool(object):
    def setupUi(self, Breast_Cancer_prediction_tool):

        self.window = Breast_Cancer_prediction_tool
        self.loadImage =Breast_Cancer_prediction_tool
        self.displayImage =Breast_Cancer_prediction_tool

        Breast_Cancer_prediction_tool.setObjectName("Breast_Cancer_prediction_tool")
        Breast_Cancer_prediction_tool.resize(648, 402)
        self.centralwidget = QtWidgets.QWidget(Breast_Cancer_prediction_tool)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_btn.setGeometry(QtCore.QRect(100, 280, 121, 51))
        self.Browse_btn.setAutoFillBackground(False)
        self.Browse_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 95);")
        self.Browse_btn.setObjectName("Browse_btn")
        self.Browse_btn.clicked.connect(self.browse)
        self.ImageBox = QtWidgets.QLabel(self.centralwidget)
        self.ImageBox.setGeometry(QtCore.QRect(36, 70, 261, 201))
        self.ImageBox.setFrameShape(QtWidgets.QFrame.Box)
        self.ImageBox.setText("")
        self.ImageBox.setObjectName("ImageBox")
        self.Predictor = QtWidgets.QLabel(self.centralwidget)
        self.Predictor.setGeometry(QtCore.QRect(380, 280, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Predictor.setFont(font)
        self.Predictor.setFrameShape(QtWidgets.QFrame.Box)
        self.Predictor.setText("")
        self.Predictor.setObjectName("Predictor")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 350, 291, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 50, 241, 161))
        self.label_2.setStyleSheet("image: url(:/newPrefix/breast-cancer-300x225.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ImageBox_2 = QtWidgets.QLabel(self.centralwidget)
        self.ImageBox_2.setGeometry(QtCore.QRect(380, 70, 261, 201))
        self.ImageBox_2.setFrameShape(QtWidgets.QFrame.Box)
        self.ImageBox_2.setText("")
        self.ImageBox_2.setObjectName("ImageBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Breast_Cancer_prediction_tool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Breast_Cancer_prediction_tool)
        self.statusbar.setObjectName("statusbar")
        Breast_Cancer_prediction_tool.setStatusBar(self.statusbar)

        self.retranslateUi(Breast_Cancer_prediction_tool)
        QtCore.QMetaObject.connectSlotsByName(Breast_Cancer_prediction_tool)

    def retranslateUi(self, Breast_Cancer_prediction_tool):
        _translate = QtCore.QCoreApplication.translate
        Breast_Cancer_prediction_tool.setWindowTitle(_translate("Breast_Cancer_prediction_tool", "Prediction Tool"))
        self.label.setText(_translate("Breast_Cancer_prediction_tool", "        Breast Cancer Prediction Tool"))
        self.Browse_btn.setText(_translate("Breast_Cancer_prediction_tool", "Browse"))
        self.label_3.setText(_translate("Breast_Cancer_prediction_tool", "  Copyright  © 2018 Stedix"))
        self.label_4.setText(_translate("Breast_Cancer_prediction_tool", "PreProcess Box"))


    def browse(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self.window,' file',"-/desktop/Images",'*.png')
        print (filepath[0])
        N = filepath[0]
        print(N)

        img = cv2.imread(N)
        img_HSV = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)
        cv2.imwrite('image/y.png',img_HSV)

        file ='D:/Final Project/Software/image/y.png'
        # print(file)
    

        

        self.window.ImageBox = QtWidgets.QLabel(self.centralwidget)
        self.window.ImageBox.setGeometry(QtCore.QRect(36, 70, 261, 201))
        self.window.ImageBox.setFrameShape(QtWidgets.QFrame.Box)
        self.window.ImageBox.setPixmap(QtGui.QPixmap(filepath[0]))
        # self.window.ImageBox.setPixmap(QtGui.QPixmap(file))
        self.window.ImageBox.show()
        

        
        self.window.ImageBox_2 =QtWidgets.QLabel(self.centralwidget)
        self.window.ImageBox_2.setGeometry(QtCore.QRect(380, 70, 261, 201))
        self.window.ImageBox_2.setFrameShape(QtWidgets.QFrame.Box)
        self.window.ImageBox_2.setPixmap(QtGui.QPixmap(file))
        self.window.ImageBox_2.show()
       


        # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # dimensions 
        img_width, img_height = 150, 150
        

        if K.image_data_format() == 'channels_first':
            input_shape = (3, img_width, img_height)
        else:
            input_shape = (img_width, img_height, 3)
        

        names = {
            0 : 'Suspicious',
            1 : 'Non-Suspicious'
        
            
        }


        # _dir =  sys.argv[1]
        _dir = str(filepath[0])
        



        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=input_shape))

        model.add(Dropout(0.2))

        model.add(Conv2D(32, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(64, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.load_weights('./models/saved_model_5.h5')

        model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])



        dir_files = glob.glob(_dir+'*.png')
        print(_dir)
        img = image.load_img(_dir, target_size=(img_width, img_height))

        x = image.img_to_array(img)

        x = np.expand_dims(x, axis=0)



        images = np.vstack([x])

        classes = model.predict(images)

        p_classes = model.predict_classes(images)
        
        
        print (names[p_classes[0][0]])
        result = names[p_classes[0][0]]
        print (result)
        # F = print (names[p_classes[0][0]])
        



        # self.Predictor = QtWidgets.QLabel(self.centralwidget)
        # self.Predictor.setGeometry(QtCore.QRect(320, 220, 191, 51))
        # self.Predictor.setFrameShape(QtWidgets.QFrame.Box)
        self.Predictor.setText(result)
        # self.Predictor.setObjectName("Predictor")
        
        # label = QtGui.QLabel(self)
        # label.setText(F)

        # self.ImageBox = QtWidgets.QLabel()
        # self.ImageBox.setGeometry(QtCore.QRect(36, 70, 311, 201))
        # self.ImageBox.setFrameShape(QtWidgets.QFrame.Box)
        # # pixmap= QtGui.QPixmap('D:/Final Project/Software/validation/non-suspicious/21.png')
        # # self.ImageBox.setPixmap(QtGui.QPixmap(filepath[0]))
        # # self.ImageBox.show()
        # self.ImageBox.setText(F)
        # self.ImageBox.setObjectName("ImageBox")
            







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Breast_Cancer_prediction_tool = QtWidgets.QMainWindow()
    ui = Ui_Breast_Cancer_prediction_tool()
    ui.setupUi(Breast_Cancer_prediction_tool)
    Breast_Cancer_prediction_tool.show()
    sys.exit(app.exec_())

