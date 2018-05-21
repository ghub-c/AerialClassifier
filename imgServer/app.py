import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import cv2
from flask_cors import CORS
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from scipy.misc import imread, imresize
import numpy as np
from operator import itemgetter




UPLOAD_FOLDER = './images'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload", methods=['POST'])
def server_info():
    image = request.files['uploads[]']
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img=cv2.imread('./images/'+filename)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(144, 256, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))

    model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['acc'])
    model.load_weights('../keras_code/saved_models/final.h5f')
    # model.save_weights('./saved_models/final.h5f')
    img = np.expand_dims(img, axis=0)
    predict = model.predict(img)
    # predict = model.predict_generator(test_batches, steps=10, verbose=2)
    first_class = predict[0][0]
    second_class = predict[0][1]
    print(predict)
    print(first_class)
    print(second_class)

    return jsonify({
        "veredict": "Private property"
    })

if __name__ == "__main__":
    app.run(port=3000)