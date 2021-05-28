from flask import Flask, jsonify, request
import os
import numpy as np
import cv2 as cv

app = Flask(__name__)


@app.route('/')
def index():
  return "<h1>Welcome to Projet fruits</h1>"

@app.route('/post/', methods=['POST'])
def post_image():
    img_array = np.fromstring(request.data, np.uint8)

    img = cv.imdecode(img_array, cv.IMREAD_COLOR)

    ##

    return jsonify({
            "re": f"Image received : {img.shape[1]}x{img.shape[0]}",
            "": ""
        })

port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995

app.run(host="0.0.0.0", threaded=True, port=port)

