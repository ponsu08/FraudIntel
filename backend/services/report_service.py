"""
Report Service

Creates a complete phishing detection report.
"""

from datetime import datetime

from agents.explainability_agent import ExplainabilityAgent
from agents.intelligence_agent import IntelligenceAgent

from services.risk_service import RiskService


explain_agent = ExplainabilityAgent()
intel_agent = IntelligenceAgent()


class ReportService:

    @staticmethod
    def generate_report(module_name, prediction_result):
        """
        Generate report for a single detector.

        prediction_result Example

        {
            "prediction":"Phishing",
            "confidence":96.3
        }
        """

        prediction = prediction_result["prediction"]
        confidence = prediction_result["confidence"]

        risk = RiskService.calculate_risk(
            prediction,
            confidence
        )

        explanation = explain_agent.explain(
            prediction,
            confidence
        )

        recommendation = intel_agent.recommend(
            prediction
        )

        return {

            "module": module_name,

            "prediction": prediction,

            "confidence": confidence,

            "risk": risk,

            "explanation": explanation,

            "recommendation": recommendation,

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }

    @staticmethod
    def generate_combined_report(results):
        """
        Create report when orchestrator combines
        Email + SMS + Website + Voice etc.
        """

        overall = RiskService.merge_results(results)

        explanation = explain_agent.explain(
            overall["overall_prediction"],
            overall["score"]
        )

        recommendation = intel_agent.recommend(
            overall["overall_prediction"]
        )

        return {

            "summary": overall,

            "results": results,

            "explanation": explanation,

            "recommendation": recommendation,

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }