import os
import joblib

from utils.feature_extractor import extract_website_features
from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class WebsiteAgent:
    def __init__(self):
        model_path = "models/website_model.pkl"

        self.model = None
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)

        self.risk = RiskAgent()
        self.explainer = ExplainabilityAgent()

    def analyze(self, url):
        # Extract website features
        features = extract_website_features(url)

        # Default prediction
        prediction = 0
        confidence = 75.0

        # Predict using trained model if available
        if self.model is not None:
            prediction = int(self.model.predict([features])[0])

            if hasattr(self.model, "predict_proba"):
                confidence = round(
                    max(self.model.predict_proba([features])[0]) * 100,
                    2,
                )

        label = "Fraud" if prediction == 1 else "Safe"

        # Calculate risk score
        risk_score = self.risk.calculate(label, confidence)

        # Generate explanation
        explanation = self.explainer.website_explanation(
            url,
            label,
        )

        return {
            "prediction": label,
            "confidence": confidence,
            "risk_score": risk_score,
            "explanation": explanation,
            "features": features,
        }