import numpy as np
import joblib
from flask import Flask, request, jsonify
import logging

# 1. Initialize Flask App
app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# 2. Load Artifacts (Model and Scaler)
try:
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
    logging.info("Model and scaler loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model artifacts: {e}")
    model = None
    scaler = None

# 3. Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({"error": "Model or scaler not loaded"}), 500

    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        
        # Input data MUST be in this order (21 features)
        # We expect the input to be a list named 'features'
        features_list = data['features']
        
        # Convert to a 2D NumPy array
        features = np.array([features_list])
        
        # 4. Scale the input data
        features_scaled = scaler.transform(features)
        
        # 5. Make prediction
        prediction = model.predict(features_scaled)
        probability = model.predict_proba(features_scaled)
        
        # 6. Return the result
        return jsonify({
            'prediction': int(prediction[0]), # 0 or 1
            'diabetes_probability': round(probability[0][1], 4) # Probability of class '1'
        })
        
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 400

# 7. Run the server
if __name__ == '__main__':
    # 'host=0.0.0.0' is required for Docker to expose the port
    app.run(host='0.0.0.0', port=5000)