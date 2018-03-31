# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from keras.preprocessing.image import ImageDataGenerator
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

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import glob
import cv2


# from PyQt5.uic import loadUi

# from cv2 import *


class Ui_Breast_Cancer_prediction_tool(object):
    def setupUi(self, Breast_Cancer_prediction_tool):
        self.window = Breast_Cancer_prediction_tool
        self.loadImage =Breast_Cancer_prediction_tool
        self.displayImage =Breast_Cancer_prediction_tool
        
        Breast_Cancer_prediction_tool.setObjectName("Breast_Cancer_prediction_tool")
        Breast_Cancer_prediction_tool.resize(800, 517)
        self.centralwidget = QtWidgets.QWidget(Breast_Cancer_prediction_tool)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 271, 41))
        self.label.setObjectName("label")
        self.Browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_btn.setGeometry(QtCore.QRect(120, 320, 75, 23))
        self.image= None
        self.Browse_btn.setObjectName("Browse_btn")
        self.Browse_btn.clicked.connect(self.browse)
        self.ImageBox = QtWidgets.QLabel(self.centralwidget)
        self.ImageBox.setGeometry(QtCore.QRect(36, 70, 311, 201))
        self.ImageBox.setFrameShape(QtWidgets.QFrame.Box)
        self.ImageBox.setText("")
        self.ImageBox.setObjectName("ImageBox")
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
    
    # @pyqtslot()

    def browse(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self.window,' file',"-/desktop/Images",'*.png')
        print (filepath[0])

        


    #     self.loadImage(filepath)

    # def loadImage1(self,fname):
    #     self.image = cv2.imread(fname)
    #     self.displayImage()
        

    #     fpath = cv2.imread(filepath,0)
    #     print (fpath) 

    #     sys.exit()

        # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # dimensions 
        img_width, img_height = 150, 150
        print('hello')

        if K.image_data_format() == 'channels_first':
            input_shape = (3, img_width, img_height)
        else:
            input_shape = (img_width, img_height, 3)
        print('hello')

        names = {
            0 : 'Suspicious',
            1 : 'Non-Suspicious'
        
            
        }


        # _dir =  sys.argv[1]
        _dir = str(filepath[0])
        print('hello')



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

        model.load_weights('./models/saved_model_4.h5')

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
            






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Breast_Cancer_prediction_tool = QtWidgets.QMainWindow()
    ui = Ui_Breast_Cancer_prediction_tool()
    ui.setupUi(Breast_Cancer_prediction_tool)
    Breast_Cancer_prediction_tool.show()
    sys.exit(app.exec_())

