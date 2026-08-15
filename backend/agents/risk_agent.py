class RiskAgent:
    """
    Calculates a normalized fraud risk score.
    """

    def calculate(self, prediction, confidence):
        """
        prediction : Fraud / Safe
        confidence : float (0-100)

        Returns:
            Risk Score (0-100)
        """

        confidence = max(0, min(confidence, 100))

        if prediction == "Fraud":

            if confidence >= 95:
                return 100

            elif confidence >= 90:
                return 95

            elif confidence >= 80:
                return 90

            elif confidence >= 70:
                return 80

            elif confidence >= 60:
                return 70

            else:
                return 60

        else:

            if confidence >= 95:
                return 5

            elif confidence >= 90:
                return 10

            elif confidence >= 80:
                return 15

            elif confidence >= 70:
                return 20

            else:
                return 30

    def level(self, risk_score):

        if risk_score >= 90:
            return "Critical"

        elif risk_score >= 75:
            return "High"

        elif risk_score >= 50:
            return "Medium"

        elif risk_score >= 25:
            return "Low"

        return "Very Low"