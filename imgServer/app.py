import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from scipy.misc import imread,imresize
import numpy as np
import cv2
from flask_cors import CORS

UPLOAD_FOLDER = './images'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload", methods=['POST'])
def server_info():
    image = request.files['uploads[]']
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    im=cv2.imread('./images/'+filename)
    print(im.shape)
    return jsonify({
        "veredict": "Private property"
    })

if __name__ == "__main__":
    app.run(port=3000)