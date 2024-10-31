from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from .utilities import Image_to_opencv, prediction
from .model_loading import load_classification_model, load_segmentation_model
from .image_processing import encode_image_to_base64
import os
import cv2
import numpy as np

BASE_DIR = "/Users/akash/Desktop/Projects/BrainCancerDetection/server/"

api = Blueprint('api', __name__)

model_seg = load_segmentation_model(BASE_DIR)
model = load_classification_model(BASE_DIR)

@api.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    file = request.files['image']

    open_cv_image = Image_to_opencv(file)

    pred = prediction(open_cv_image, model, model_seg)
    if pred is not None:
        pred = np.asarray(pred)[0].squeeze().round()

        open_cv_image = cv2.resize(open_cv_image, (256,256))
        open_cv_image[pred==1] = (0,255,0)

        encoded_image = encode_image_to_base64(open_cv_image.copy())

        return jsonify({"message": "Image processed", "processedImage": f"data:image/png;base64,{encoded_image}"}), 200
    else:
        return jsonify({"message": None, "processedImage": "No tumor detected"})