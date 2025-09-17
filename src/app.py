from flask import Flask, request, jsonify
import os
import pickle
from model.predict import make_prediction

app = Flask(__name__)

# Load the trained model (resilient if missing)
model = None
model_path_options = [
    'src/model/model.pkl',  # local dev
    'model/model.pkl',      # container workdir
]
for _path in model_path_options:
    if os.path.exists(_path):
        with open(_path, 'rb') as f:
            model = pickle.load(f)
        break


@app.route('/health', methods=['GET'])
def health_check():
    status = 'healthy' if model is not None else 'model_missing'
    return jsonify({'status': status}), 200


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            raise RuntimeError('Model not loaded')
        data = request.get_json()
        prediction = make_prediction(model, data)
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

