from fastapi import APIRouter
from pydantic import BaseModel

from agents.intelligence_agent import IntelligenceAgent

router = APIRouter()

agent = IntelligenceAgent()


class AnalysisRequest(BaseModel):
    type: str
    data: dict


@router.post("/")
def analyze(request: AnalysisRequest):
    """
    Main endpoint that routes the request
    to the appropriate AI agent.
    """

    result = agent.process(
        request.type,
        request.data
    )

    return {
        "success": True,
        "analysis_type": request.type,
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "Orchestrator",
        "status": "Running"
    }