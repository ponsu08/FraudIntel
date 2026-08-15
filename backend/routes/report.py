from fastapi import APIRouter
from pydantic import BaseModel

from services.report_service import ReportService

router = APIRouter()

report_service = ReportService()


class ReportRequest(BaseModel):
    module: str
    prediction: str
    confidence: float
    risk_score: float
    explanation: str
    details: dict = {}


@router.post("/generate")
def generate_report(request: ReportRequest):
    """
    Generate a fraud analysis report.
    """

    report = report_service.generate_report(
        module=request.module,
        prediction=request.prediction,
        confidence=request.confidence,
        risk_score=request.risk_score,
        explanation=request.explanation,
        details=request.details
    )

    return {
        "success": True,
        "report": report
    }


@router.get("/health")
def health():
    return {
        "module": "Report",
        "status": "Running"
    }