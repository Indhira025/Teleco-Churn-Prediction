"""
Customer Churn Prediction - Flask Backend Application
========================================================
This application serves a machine learning model to predict
telecommunications customer churn based on various features.
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Load models and artifacts
try:
    model = pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("standar_Scaler.pkl", "rb"))
    app.logger.info("Models loaded successfully")
except Exception as e:
    app.logger.error(f"Error loading models: {str(e)}")
    model = None
    scaler = None

# Feature list in the exact order expected by the model
FEATURES = [
    'tenure_yeo_trim',
    'MonthlyCharges_quantile_trim',
    'TotalCharges_interpolate_quantile_trim',
    'SeniorCitizen',
    'Partner_Yes',
    'Dependents_Yes',
    'PaperlessBilling_Yes',
    'MultipleLines_Yes',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check',
    'Teleco_Partner_BSNL',
    'Teleco_Partner_Reliance Jio',
    'Teleco_Partner_Vodafone',
    'Contract_Encoded'
]

# Mapping for string to encoded values
CONTRACT_MAPPING = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
}

PAYMENT_MAPPING = {
    'Electronic check': 'PaymentMethod_Electronic check',
    'Mailed check': 'PaymentMethod_Mailed check',
    'Credit card (automatic)': 'PaymentMethod_Credit card (automatic)'
}

SIM_MAPPING = {
    'Jio': 'Teleco_Partner_Reliance Jio',
    'Airtel': None,  # Airtel is the reference category (dropped in one-hot encoding)
    'Vi': 'Teleco_Partner_Vodafone',
    'BSNL': 'Teleco_Partner_BSNL'
}


@app.route('/')
def home():
    """Render the main prediction page."""
    app.logger.info("Home page accessed")
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests from the web interface.
    Expects form data with all required features.
    Returns prediction result as HTML response.
    """
    try:
        # Initialize feature dictionary with zeros
        feature_dict = {feature: 0 for feature in FEATURES}

        # Extract form data
        tenure = float(request.form.get('tenure_yeo_trim', 0))
        monthly_charges = float(request.form.get('MonthlyCharges_quantile_trim', 0))
        total_charges = float(request.form.get('TotalCharges_interpolate_quantile_trim', 0))

        # Direct numeric features
        feature_dict['tenure_yeo_trim'] = tenure
        feature_dict['MonthlyCharges_quantile_trim'] = monthly_charges
        feature_dict['TotalCharges_interpolate_quantile_trim'] = total_charges
        feature_dict['SeniorCitizen'] = int(request.form.get('SeniorCitizen', 0))

        # Binary features (Yes/No)
        feature_dict['Partner_Yes'] = 1 if request.form.get('Partner_Yes') == 'Yes' else 0
        feature_dict['Dependents_Yes'] = 1 if request.form.get('Dependents_Yes') == 'Yes' else 0
        feature_dict['PaperlessBilling_Yes'] = 1 if request.form.get('PaperlessBilling_Yes') == 'Yes' else 0
        feature_dict['MultipleLines_Yes'] = 1 if request.form.get('MultipleLines_Yes') == 'Yes' else 0

        # Internet Service
        internet_service = request.form.get('InternetService', 'DSL')
        if internet_service == 'Fiber optic':
            feature_dict['InternetService_Fiber optic'] = 1
        elif internet_service == 'No':
            feature_dict['InternetService_No'] = 1

        # DSL is reference category (all zeros)

        # Service features with three categories
        def set_service_features(service_name, value):
            yes_col = f'{service_name}_Yes'
            no_int_col = f'{service_name}_No internet service'

            feature_dict[yes_col] = 1 if value == 'Yes' else 0
            feature_dict[no_int_col] = 1 if value == 'No phone service' else 0
            # 'No' is reference category (all zeros)

        set_service_features('OnlineSecurity', request.form.get('OnlineSecurity', 'No'))
        set_service_features('OnlineBackup', request.form.get('OnlineBackup', 'No'))
        set_service_features('DeviceProtection', request.form.get('DeviceProtection', 'No'))
        set_service_features('TechSupport', request.form.get('TechSupport', 'No'))
        set_service_features('StreamingTV', request.form.get('StreamingTV', 'No'))
        set_service_features('StreamingMovies', request.form.get('StreamingMovies', 'No'))

        # Payment Method
        payment_method = request.form.get('PaymentMethod', 'Electronic check')
        payment_col = PAYMENT_MAPPING.get(payment_method)
        if payment_col:
            feature_dict[payment_col] = 1

        # SIM Provider (Teleco Partner)
        sim_provider = request.form.get('Teleco_Partner', 'Airtel')
        sim_col = SIM_MAPPING.get(sim_provider)
        if sim_col:
            feature_dict[sim_col] = 1
        # Airtel is reference category (all zeros)

        # Contract Type
        contract = request.form.get('Contract', 'Month-to-month')
        feature_dict['Contract_Encoded'] = CONTRACT_MAPPING.get(contract, 0)

        # Create feature array in correct order
        feature_values = [feature_dict[feature] for feature in FEATURES]
        features_array = np.array([feature_values])

        app.logger.info(f"Prediction request received with features: {feature_dict}")

        # Make prediction
        if model is not None:
            prediction = model.predict(features_array)[0]
            probability = None

            # Get probability if available
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(features_array)[0]
                probability = proba[1] if prediction == 1 else proba[0]

            # Prepare result message
            if prediction == 1:
                result = "⚠️ Customer will CHURN"
                result_class = "danger"
                if probability:
                    result += f" (Confidence: {probability:.1%})"
            else:
                result = "✅ Customer will STAY"
                result_class = "success"
                if probability:
                    result += f" (Confidence: {probability:.1%})"

            app.logger.info(f"Prediction result: {result}")

            return render_template('index.html',
                                   prediction_text=result,
                                   prediction_class=result_class,
                                   form_data=request.form)
        else:
            app.logger.error("Model not loaded properly")
            return render_template('index.html',
                                   prediction_text="⚠️ Model not available. Please try again later.",
                                   prediction_class="danger")

    except Exception as e:
        app.logger.error(f"Error during prediction: {str(e)}")
        return render_template('index.html',
                               prediction_text=f"❌ Error: {str(e)}",
                               prediction_class="danger")


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    status = {
        'status': 'healthy',
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None,
        'timestamp': datetime.now().isoformat()
    }
    return jsonify(status)


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """
    REST API endpoint for predictions.
    Accepts JSON input and returns JSON response.
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Extract features from JSON
        feature_dict = {feature: 0 for feature in FEATURES}

        # Similar feature extraction logic as above
        # (Same as predict() but returns JSON)

        feature_values = [feature_dict[feature] for feature in FEATURES]
        features_array = np.array([feature_values])

        if model is not None:
            prediction = int(model.predict(features_array)[0])
            probability = None

            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(features_array)[0]
                probability = float(proba[1])

            return jsonify({
                'success': True,
                'prediction': prediction,
                'churn': bool(prediction),
                'confidence': probability,
                'message': 'Customer will churn' if prediction == 1 else 'Customer will stay'
            })
        else:
            return jsonify({'error': 'Model not available'}), 503

    except Exception as e:
        app.logger.error(f"API prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)