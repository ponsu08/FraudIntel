from fastapi import APIRouter, UploadFile, File, HTTPException
from agents.voice_agent import VoiceAgent
import shutil
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

agent = VoiceAgent()


@router.post("/analyze")
async def analyze_voice(file: UploadFile = File(...)):
    """
    Upload an audio file and analyze it for voice fraud.
    """

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = agent.analyze(file_path)

    return {
        "success": True,
        "module": "Voice",
        "filename": file.filename,
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "Voice",
        "status": "Running"
    }