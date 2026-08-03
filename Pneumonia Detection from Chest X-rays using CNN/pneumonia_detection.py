import os
import numpy as np
import pandas as pd
from PIL import Image
import cv2

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19


# -----------------------------
# Build VGG19 model
# -----------------------------

base_model = VGG19(
    include_top=False,
    input_shape=(128, 128, 3)
)

x = base_model.output

flat = Flatten()(x)

class_1 = Dense(
    4608,
    activation="relu"
)(flat)

dropout = Dropout(0.2)(class_1)

class_2 = Dense(
    1152,
    activation="relu"
)(dropout)

output = Dense(
    2,
    activation="softmax"
)(class_2)

model_03 = Model(
    base_model.inputs,
    output
)


# -----------------------------
# Load trained model weights
# -----------------------------

model_03.load_weights(
    r"E:\All My Projects\Projects\Pneumonia Detection from Chest X-rays using CNN\model_weights\vgg19_model_01.keras"
)

print("Model loaded successfully.")


# -----------------------------
# Flask app
# -----------------------------

app = Flask(__name__)


# -----------------------------
# Helper function
# -----------------------------

def get_className(classNo):

    if classNo == 0:
        return "Normal"

    elif classNo == 1:
        return "Pneumonia"


# -----------------------------
# Prediction function
# -----------------------------

def get_result(img):

    image = cv2.imread(img)

    if image is None:
        raise ValueError("Unable to read image")

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize
    image = cv2.resize(image, (128, 128))

    # Normalize exactly like training
    image = image.astype("float32") / 255.0

    # Add batch dimension
    input_img = np.expand_dims(image, axis=0)

    # Prediction
    result = model_03.predict(
        input_img,
        verbose=0
    )

    # Get class with highest probability
    result01 = np.argmax(
        result,
        axis=1
    )

    return result01[0]


# -----------------------------
# Home page
# -----------------------------

@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


# -----------------------------
# Prediction route
# -----------------------------

@app.route("/predict", methods=["POST", "GET"])
def upload():

    if request.method == "POST":

        try:

            file = request.files["file"]

            base_path = os.path.dirname(__file__)

            upload_folder = os.path.join(
                base_path,
                "uploads"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            file_path = os.path.join(
                upload_folder,
                secure_filename(file.filename)
            )

            file.save(file_path)

            value = get_result(file_path)

            result = get_className(value)

            return result

        except Exception as e:

            print(f"Error: {e}")

            return "Error processing image"

    return None


# -----------------------------
# Run Flask
# -----------------------------

if __name__ == "__main__":

    app.run(debug=True)