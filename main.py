import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Hides TensorFlow info and warnings

import logging
logging.basicConfig(level=logging.WARNING, filename="warnings.txt")



import numpy as np
from tensorflow import nn, expand_dims
from tensorflow.keras import utils, models

loaded_model = models.load_model('model.keras')

def main():
    img_dir = input("Please input the path to the image that you wish to predict: ")

    img = utils.load_img(img_dir, target_size=(180, 180))

    img_array = utils.img_to_array(img)
    img_array = expand_dims(img_array, 0)

    predictions = loaded_model.predict(img_array, verbose=0)

    score = nn.softmax(predictions[0])

    class_names = ['cats', 'dogs']

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
)
    


main()