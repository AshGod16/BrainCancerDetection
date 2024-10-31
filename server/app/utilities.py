import pandas as pd
import numpy as np
import seaborn as sns
import cv2
import tensorflow as tf
import os 
from PIL import Image
from tensorflow.keras import backend as K
from keras.utils import register_keras_serializable

def prediction(img, model, model_seg):
    '''
    Predcition function which takes dataframe containing ImageID as Input and perform 2 type of prediction on the image
    Initially, image is passed through the classification network which predicts whether the image has defect or not, if the model
    is 99% sure that the image has no defect, then the image is labeled as no-defect, if the model is not sure, it passes the image to the
    segmentation network, it again checks if the image has defect or not, if it has defect, then the type and location of defect is found
    '''

    #Normalizing the image
    img = img * 1./255.

    #Reshaping the image
    img = cv2.resize(img,(256,256))

    #Converting the image into array
    img = np.array(img, dtype = np.float64)

    #reshaping the image from 256,256,3 to 1,256,256,3
    img = np.reshape(img, (1,256,256,3))

    # is_defect = model.predict(img)

    # #if tumour is not present we append the details of the image to the list
    # if np.argmax(is_defect) == 0:
    # #   print('here')
    #   return None

    #Creating a empty array of shape 1,256,256,1
    X = np.empty((1, 256, 256, 3))

    #standardising the image
    img -= img.mean()
    img /= img.std()

    #converting the shape of image from 256,256,3 to 1,256,256,3
    X[0,] = img

    #make prediction
    predict = model_seg.predict(X)

    print("SUM", predict.round().astype(int).sum())

    #if the sum of predicted values is equal to 0 then there is no tumour
    if predict.round().astype(int).sum() < 1400:
        return None
    else:
    #if the sum of pixel values are more than 0, then there is tumour
        return predict

@register_keras_serializable(package='Custom', name='focal_tversky')
def tversky(y_true, y_pred, smooth = 1e-6):
    y_true = K.cast(y_true, 'float32')
    y_pred = K.cast(y_pred, 'float32')
    y_true_pos = K.flatten(y_true)
    y_pred_pos = K.flatten(y_pred)
    true_pos = K.sum(y_true_pos * y_pred_pos)
    false_neg = K.sum(y_true_pos * (1-y_pred_pos))
    false_pos = K.sum((1-y_true_pos)*y_pred_pos)
    alpha = 0.7
    return (true_pos + smooth)/(true_pos + alpha*false_neg + (1-alpha)*false_pos + smooth)

def tversky_loss(y_true, y_pred):
    return 1 - tversky(y_true,y_pred)

def focal_tversky(y_true,y_pred):
    pt_1 = tversky(y_true, y_pred)
    gamma = 0.75
    return K.pow((1-pt_1), gamma)

def Image_to_opencv(file):
    image = Image.open(file.stream)
    img = image.convert('RGB')
    open_cv_image = np.array(img)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    return open_cv_image