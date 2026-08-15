import os
import joblib

from utils.ocr import decode_qr
from utils.url_checker import check_url
from utils.feature_extractor import extract_qr_features

from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class QRAgent:
    def __init__(self):
        model_path = "models/qr_model.pkl"

        self.model = None
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)

        self.risk = RiskAgent()
        self.explainer = ExplainabilityAgent()

    def analyze(self, image_path):
        # Decode QR code
        qr_content = decode_qr(image_path)

        if not qr_content:
            return {
                "prediction": "Unknown",
                "confidence": 0,
                "risk_score": 0,
                "decoded_data": None,
                "url_analysis": None,
                "explanation": "No QR code could be detected in the uploaded image.",
                "features": None,
            }

        # Analyze URL
        url_info = check_url(qr_content)

        # Extract ML features
        features = extract_qr_features(qr_content, url_info)

        # Default values
        prediction = 0
        confidence = 80.0

        # Predict if model exists
        if self.model is not None:
            prediction = int(self.model.predict([features])[0])

            if hasattr(self.model, "predict_proba"):
                confidence = round(
                    max(self.model.predict_proba([features])[0]) * 100,
                    2,
                )

        label = "Fraud" if prediction == 1 else "Safe"

        risk_score = self.risk.calculate(label, confidence)

        explanation = self.explainer.qr_explanation(
            qr_content,
            label,
        )

        return {
            "prediction": label,
            "confidence": confidence,
            "risk_score": risk_score,
            "decoded_data": qr_content,
            "url_analysis": url_info,
            "features": features,
            "explanation": explanation,
        }