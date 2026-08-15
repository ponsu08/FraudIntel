import os
import joblib

from utils.feature_extractor import extract_social_features
from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class SocialAgent:

    def __init__(self):

        model_path = "models/social_model.pkl"

        self.model = (
            joblib.load(model_path)
            if os.path.exists(model_path)
            else None
        )

        self.risk = RiskAgent()

        self.explainer = ExplainabilityAgent()

    def analyze(self, text, username=""):

        # Feature Extraction
        features = extract_social_features(
            text,
            username
        )

        # ML Prediction
        if self.model:

            prediction = self.model.predict([features])[0]

            confidence = round(
                max(
                    self.model.predict_proba([features])[0]
                ) * 100,
                2,
            )

        else:

            prediction = 0
            confidence = 85.0

        label = "Fraud" if prediction == 1 else "Safe"

        # Calculate Risk Score
        risk_score = self.risk.calculate(
            label,
            confidence
        )

        # Generate Explainability
        explanation = self.explainer.social_explanation(
            text,
            username,
            label
        )

        return {

            "prediction": label,

            "confidence": confidence,

            "risk_score": risk_score,

            "username": username,

            "text": text,

            "explanation": explanation,

            "features": features
        }