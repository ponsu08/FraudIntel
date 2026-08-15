"""
Website Phishing Detection Service
"""

import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "website_model.pkl"
)

SCALER_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "scaler.pkl"
)

website_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


class WebsiteService:

    @staticmethod
    def predict(features: dict):

        required = [
            "url_length",
            "num_dots",
            "has_https",
            "num_special_chars"
        ]

        for field in required:
            if field not in features:
                return {
                    "success": False,
                    "message": f"{field} is missing."
                }

        values = np.array([
            [
                features["url_length"],
                features["num_dots"],
                features["has_https"],
                features["num_special_chars"]
            ]
        ])

        values = scaler.transform(values)

        prediction = website_model.predict(values)[0]

        try:
            probability = website_model.predict_proba(values)[0]
            confidence = round(max(probability) * 100, 2)
        except Exception:
            confidence = None

        return {
            "success": True,
            "prediction": int(prediction),
            "label": "Phishing" if prediction == 1 else "Safe Website",
            "confidence": confidence
        }