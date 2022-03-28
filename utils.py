import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

## global  variable

## dataset

def load_dataset():
    IMG_HEIGHT=28
    IMG_WIDTH=28
    #input_shape=(IMG_HEIGHT,IMG_WIDTH,1)
    
    ##
    (x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
    ##
    x_train=x_train.reshape(x_train.shape[0],IMG_HEIGHT,IMG_WIDTH,1)
    x_test=x_test.reshape(x_test.shape[0],IMG_HEIGHT,IMG_WIDTH,1)

    x_train=x_train.astype('float32')
    x_test=x_test.astype('float32')

    x_train=x_train/255
    x_test=x_test/255

    return x_train, x_test,y_test


## Model (load)
def load_model(model_path):
    return tf.keras.models.load_model(model_path)



## Features Extraction
def intermediate(model, layer, X_train):
    X = model.input
    Y = model.get_layer(layer).output
    temp_model = tf.keras.models.Model(X,Y)

    x_temp = X_train[:9]
    res = temp_model.predict(x_temp)
    shape = res.shape
    return res, shape
