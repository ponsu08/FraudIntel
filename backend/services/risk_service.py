"""
Risk Service

Uses the Risk Agent to calculate an overall phishing/fraud risk score.
"""

from agents.risk_agent import RiskAgent


risk_agent = RiskAgent()


class RiskService:
    """
    Service responsible for computing overall risk.
    """

    @staticmethod
    def calculate_risk(prediction, confidence):
        """
        Parameters
        ----------
        prediction : str
            Safe / Phishing / Fraudulent

        confidence : float
            Model confidence (0-100)

        Returns
        -------
        dict
        """

        return risk_agent.calculate(
            prediction=prediction,
            confidence=confidence
        )

    @staticmethod
    def merge_results(results):
        """
        Combine multiple module outputs.

        Example:
        [
            {"prediction":"Safe","confidence":88},
            {"prediction":"Phishing","confidence":97}
        ]
        """

        if not results:
            return {
                "overall_prediction": "Unknown",
                "overall_risk": "Low",
                "score": 0
            }

        scores = []

        for item in results:
            confidence = item.get("confidence", 0)

            if item.get("prediction", "").lower() in [
                "phishing",
                "fraud",
                "fraudulent",
                "malicious"
            ]:
                scores.append(confidence)
            else:
                scores.append(100 - confidence)

        average = sum(scores) / len(scores)

        risk = risk_agent.score_to_level(average)

        return {
            "overall_prediction": (
                "Phishing"
                if average >= 50
                else "Safe"
            ),
            "overall_risk": risk,
            "score": round(average, 2)
        }