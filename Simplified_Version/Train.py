import os
import cv2
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.utils import normalize
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Activation,Dropout,Flatten,Dense

img_dir = 'D:/Brain Tumor project/Dataset'

no_tmr= os.listdir(img_dir+'/no')
yes_tmr= os.listdir(img_dir+'/yes')
dataset=[]
label=[]
Input_size = 64

for i,img_name in  enumerate(no_tmr):
    if (img_name.split('.')[1]=='jpg'):
        image = cv2.imread(img_dir+'/no'+'/'+img_name)
        image = Image.fromarray(image,'RGB')
        image = image.resize((Input_size,Input_size))
        dataset.append(np.array(image))
        label.append(0)
        
for i,img_name in  enumerate(yes_tmr):
    if (img_name.split('.')[1]=='jpg'):
        image = cv2.imread(img_dir+'/yes'+'/'+img_name)
        image = Image.fromarray(image,'RGB')
        image = image.resize((Input_size,Input_size))
        dataset.append(np.array(image))
        label.append(1)
    
dataset = np.array(dataset)
label = np.array(label)

X_train,X_test,Y_train,Y_test = train_test_split(dataset,label,test_size=0.2,random_state=0)

X_train = normalize(X_train,axis=1)
X_test = normalize(X_test,axis=1)
   
# Model Building

model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = (Input_size,Input_size,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model = Sequential()
model.add(Conv2D(32,(3,3),kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model = Sequential()
model.add(Conv2D(32,(3,3),kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer = 'adam',metrics=['accuracy'])

model.fit(X_train,Y_train,batch_size=32,verbose = 1,epochs=10,validation_data=(X_test,Y_test),shuffle=True)

model.save('Brain_Tumor10eps.h5')
