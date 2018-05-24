from flask import Flask, jsonify, request
import os
from werkzeug.utils import secure_filename
import cv2
import math
from flask_cors import CORS
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

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def function(option):
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
    model.add(Dense(option, activation='softmax'))
    return model

@app.route("/upload", methods=['POST'])
def server_info():
    image = request.files['uploads[]']
    option=int(request.args.get('option'))
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img=cv2.imread('./images/'+filename)

    model=function(option)
    model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['acc'])
    if (option==2):
        model.load_weights('../keras_code/saved_models/final.h5f')
    else:
        model.load_weights('../keras_code/saved_models/finalMulti.h5f')
    # model.save_weights('./saved_models/final.h5f')
    img = np.expand_dims(img, axis=0)
    predict = model.predict(img)
    # predict = model.predict_generator(test_batches, steps=10, verbose=2)
    first_class = predict[0][0]
    second_class = predict[0][1]
    print(predict)
    print(first_class)
    print(second_class)
    if (option==3):
        third_class=predict[0][2]
        Grass=third_class * 100

    Street = first_class * 100
    Private_propierty =  second_class * 100

    if (option==2):
        return jsonify({

            "street": truncate(Street, 5),
            "property": truncate(Private_propierty,5)
        })
    else:
        return jsonify({

            "street": truncate(Street, 5),
            "property": truncate(Private_propierty, 5),
            "grass": truncate(Grass,5)
        })

if __name__ == "__main__":
    app.run(port=3000)