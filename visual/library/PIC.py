"""
The Pet Image Classifinator (PIC) is a library for the image classification model developed for the Pettodex Pet Pokedext project.

This library contains the following methods:
- classify(path: str) -> str: Takes in a URL path as input and returns its classification as a string.

Proper Usage:
Make sure that this file is in the same folder as the PIC.weights.h5 file, which contains the model weights for the CNN visual classification model.
"""

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def classify(path: str) -> str:
    """
    The classify method takes in a URL path for a single image and returns its classification on a string.
    """

    # Create model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(10)
    ])

    # Preprocess image
    # Download the image
    response = requests.get(path)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))

    # Resize and preprocess image
    img = img.resize((32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Load model
    model_path = "PIC.weights.h5"
    model.load_weights(model_path)

    # Predict classification for current image
    predictions = model.predict(img_array)
    class_names = [
        'other',
        'other',
        'bird',
        'cat',
        'deer',
        'dog',
        'frog',
        'horse',
        'other',
        'other'
    ]
    probabilities = tf.nn.softmax(predictions).numpy()
    predicted_class_index = np.argmax(probabilities)
    predicted_class_label = class_names[predicted_class_index]

    return predicted_class_label


