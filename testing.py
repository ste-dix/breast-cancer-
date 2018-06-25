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

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

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


_dir =  sys.argv[1]



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

for _file in dir_files:
    file_path = _file
    

    img = image.load_img(file_path, target_size=(img_width, img_height))
    
    x = image.img_to_array(img)
    
    x = np.expand_dims(x, axis=0)

    

    images = np.vstack([x])

    classes = model.predict(images)
    
    p_classes = model.predict_classes(images)
    print (names[p_classes[0][0]])
    
