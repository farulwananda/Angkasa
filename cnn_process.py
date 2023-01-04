from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
from numpy import array
from numpy import argmax


model = None


def load_data():
    model = load_model("model/model_t19.h5")
    print("Model Load Successfuly")
    return model


class_predictions = array([
    'basal',
    'melanoma',
    'normal',
    'vascular'
])


def read_image(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image


def predicts(image: Image.Image):
    global model
    if model is None:
        model = load_data()

    image = np.asarray(image.resize((64, 64)))[..., :3]
    image_array = img_to_array(image)
    image_array = image_array / 255.

    image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))
    result = model.predict(image_array)

    score = tf.nn.softmax(result[0])
    confidence = max(score)

    print("Result is ", score)
    print(
        "This image is {}"
        .format(class_predictions[np.argmax(score)])
    )
    print("Confidence is", confidence)

    return class_predictions[np.argmax(score)]


