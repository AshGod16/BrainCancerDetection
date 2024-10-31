from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import cv2
from flask_cors import cross_origin
import numpy as np
from app import *
import base64
import os

app = Flask(__name__)

app.register_blueprint(api)
# CORS(app)  # This will allow CORS for all routes

if __name__ == '__main__':
    app.run(debug=True)
