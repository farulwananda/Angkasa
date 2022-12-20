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
    model = load_model("model/model_x3.h5")
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
    img_array = img_to_array(image)
    img_array = img_array / 255.

    # result = decode_predictions(model.predict(img_array), 2)[0]
    img_array = img_array.reshape((1, img_array.shape[0], img_array.shape[1], img_array.shape[2]))
    result = model.predict(img_array)

    score = tf.nn.softmax(result[0])
    confidence = max(score)

    print("Result is ", score)
    print(
        "This image belongs to {}"
        .format(class_predictions[np.argmax(score)])
    )
    print("Confidence is", confidence)

    return class_predictions[np.argmax(score)]


