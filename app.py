import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template  # <-- Added render_template
import logging
import traceback

# 1. Initialize Flask App
# (Flask automatically looks for a 'templates' folder)
app = Flask(__name__)

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# 2. Load Artifacts
try:
    logging.info("Attempting to load diabetes_model.pkl...")
    model = joblib.load("diabetes_model.pkl")
    logging.info("Model loaded successfully.")

    logging.info("Attempting to load scaler.pkl...")
    scaler = joblib.load("scaler.pkl")
    logging.info("Scaler loaded successfully.")

except Exception as e:
    logging.error(f"Error loading model artifacts: {e}")
    logging.error(traceback.format_exc())
    model = None
    scaler = None


# --- NEW: Route for the Web Page ---
@app.route('/')
def home():
    return render_template('index.html')


# 3. Prediction Endpoint (unchanged)
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({"error": "Model or scaler not loaded."}), 500

    try:
        data = request.get_json(force=True)
        features_list = data['features']
        features = np.array([features_list])

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)
        probability = model.predict_proba(features_scaled)

        return jsonify({
            'prediction': int(prediction[0]),
            'diabetes_probability': round(probability[0][1], 4)
        })

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)