"""
QR Code Phishing Detection Service

Loads the trained QR phishing model and predicts whether
a QR code is safe or phishing.
"""

import os
import joblib
import numpy as np


# ------------------------------------------------------
# Model Paths
# ------------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "qr_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "scaler.pkl"
)

# ------------------------------------------------------
# Load Model
# ------------------------------------------------------

qr_model = joblib.load(MODEL_PATH)

scaler = joblib.load(SCALER_PATH)


# ------------------------------------------------------
# QR Service
# ------------------------------------------------------

class QRService:

    @staticmethod
    def predict(features: dict):
        """
        Predict whether a QR code is phishing.

        Required Features:
        ------------------
        url_length
        has_https
        num_special_chars
        qr_complexity
        """

        required_features = [
            "url_length",
            "has_https",
            "num_special_chars",
            "qr_complexity"
        ]

        # Check missing values
        for feature in required_features:

            if feature not in features:

                return {
                    "success": False,
                    "message": f"Missing feature: {feature}"
                }

        # Convert to numpy array
        X = np.array([[
            features["url_length"],
            features["has_https"],
            features["num_special_chars"],
            features["qr_complexity"]
        ]])

        # Scale
        X = scaler.transform(X)

        # Prediction
        prediction = qr_model.predict(X)[0]

        # Confidence
        try:

            probability = qr_model.predict_proba(X)[0]

            confidence = round(
                max(probability) * 100,
                2
            )

        except Exception:

            confidence = None

        return {

            "success": True,

            "prediction": int(prediction),

            "label": (
                "Phishing QR Code"
                if prediction == 1
                else "Safe QR Code"
            ),

            "confidence": confidence
        }