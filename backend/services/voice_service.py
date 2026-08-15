"""
Voice Phishing (Vishing) Detection Service
"""

import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "voice_model.pkl"
)

SCALER_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "scaler.pkl"
)

voice_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


class VoiceService:

    @staticmethod
    def predict(features: dict):

        required = [
            "duration",
            "num_suspicious_words",
            "urgency_score",
            "caller_reputation"
        ]

        for field in required:
            if field not in features:
                return {
                    "success": False,
                    "message": f"{field} is missing."
                }

        values = np.array([
            [
                features["duration"],
                features["num_suspicious_words"],
                features["urgency_score"],
                features["caller_reputation"]
            ]
        ])

        values = scaler.transform(values)

        prediction = voice_model.predict(values)[0]

        try:
            probability = voice_model.predict_proba(values)[0]
            confidence = round(max(probability) * 100, 2)
        except Exception:
            confidence = None

        return {
            "success": True,
            "prediction": int(prediction),
            "label": "Vishing" if prediction == 1 else "Safe Call",
            "confidence": confidence
        }