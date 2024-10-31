from .utilities import focal_tversky, tversky
import tensorflow as tf
import os
from flask import current_app

def load_segmentation_model(base_dir):
    # Load model
    model_path = os.path.join(base_dir, 'models/ResUNet-model.json')
    weights_path = os.path.join(base_dir, 'weights/ResUNet-weights.keras')

    with open(model_path, 'r') as json_file:
        json_savedModel= json_file.read()
    # load the model architecture 
    model_seg = tf.keras.models.model_from_json(json_savedModel)
    model_seg.load_weights(weights_path)
    adam = tf.keras.optimizers.Adam(learning_rate = 0.05, epsilon = 0.1)
    model_seg.compile(optimizer = adam, loss = focal_tversky, metrics = [tversky])

    return model_seg

def load_classification_model(base_dir):
    model_path = os.path.join(base_dir, 'models/classifier-resnet-model.json')
    weights_path = os.path.join(base_dir, 'weights/classifier-resnet-weights.keras')
    
    with open(model_path, 'r') as json_file:
        json_savedModel= json_file.read()
    # load the model  
    model = tf.keras.models.model_from_json(json_savedModel)
    model.load_weights(weights_path)
    model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics= ["accuracy"])
    return model