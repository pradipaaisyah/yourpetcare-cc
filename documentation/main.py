from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image

import os
import numpy as np
import tensorflow as tf

app = Flask('__name__')
app.config['DEBUG'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

model = tf.keras.models.load_model('saved_model/')
with open('labels.txt', 'r') as label:
    labels = label.read().splitlines()

@app.route('/')
def loadPage():
    return 'Hello!'

@app.route('/predict', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400

        # Get file
        file = request.files['file']
        filename = secure_filename(file.filename)
        path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path_file)

        # Process image
        img = Image.open(path_file).resize((224, 224))
        x = np.array(img).astype(np.float32) / 255.0
        x = np.expand_dims(x, axis=0)

        # Predict
        result = model.predict(x)
        predicted = labels[np.argmax(result[0])]

        response = {
            'message': 'success',
            'predicted': predicted,
            'confidence': result[0][np.argmax(result[0])] * 100
        }

        return jsonify(response), 200


if __name__ == '__main__':
    app.run()
