from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import cv2
from flask_cors import cross_origin
import numpy as np
from utilities import *
import base64

app = Flask(__name__)
# CORS(app)  # This will allow CORS for all routes

# Load model
with open('models/ResUNet-model.json', 'r') as json_file:
    json_savedModel= json_file.read()
# load the model architecture 
model_seg = tf.keras.models.model_from_json(json_savedModel)
model_seg.load_weights('weights/ResUNet-weights.keras')
adam = tf.keras.optimizers.Adam(learning_rate = 0.05, epsilon = 0.1)
model_seg.compile(optimizer = adam, loss = focal_tversky, metrics = [tversky])

with open('models/classifier-resnet-model.json', 'r') as json_file:
    json_savedModel= json_file.read()
# load the model  
model = tf.keras.models.model_from_json(json_savedModel)
model.load_weights('weights/classifier-resnet-weights.keras')
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics= ["accuracy"])

def encode_image_to_base64(image):
    if len(image.shape) == 2:  # Grayscale
        image = Image.fromarray(image)
    else:  # RGB or RGBA
        image = Image.fromarray(image, 'RGB')

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    image = Image.open(file.stream)
    img = image.convert('RGB')
    open_cv_image = np.array(img)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    pred = prediction(open_cv_image, model, model_seg)
    if pred is not None:
        pred = np.asarray(pred)[0].squeeze().round()

        open_cv_image = cv2.resize(open_cv_image, (256,256))
        open_cv_image[pred==1] = (0,255,0)

        encoded_image = encode_image_to_base64(open_cv_image.copy())

        return jsonify({"message": "Image processed", "processedImage": f"data:image/png;base64,{encoded_image}"}), 200
    else:
        return jsonify({"message": None, "processedImage": "No tumor detected"})

if __name__ == '__main__':
    app.run(debug=True)
