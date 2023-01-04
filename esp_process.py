from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
from numpy import array
from numpy import argmax
import os
import glob

model = None


def load_data():
    model = load_model("model/model_x3.h5")
    print("Model Load Successfuly")
    return model


class_predictions = array([
    'basal',
    'melanoma',
    'normal',
    'vascular'
])


def predictx(latest_file):
    global model
    if model is None:
        model = load_data()
    img = image.load_img(latest_file, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    lmao = img_batch / 255.

    result = model.predict(lmao)
    score = tf.nn.softmax(result[0])

    print(latest_file)
    print(
        "This image is {}"
        .format(class_predictions[np.argmax(score)])
    )
    # img = cv2.imread(filename)
    # img_array = Image.fromarray(img)
    # img = read_image(img)
    # prediction = predicts(img)

    return class_predictions[np.argmax(score)]
