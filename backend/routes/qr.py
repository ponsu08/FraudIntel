from fastapi import APIRouter, UploadFile, File
from agents.qr_agent import QRAgent
import shutil
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

agent = QRAgent()


@router.post("/analyze")
async def analyze_qr(file: UploadFile = File(...)):
    """
    Upload QR Code Image
    """

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = agent.analyze(file_path)

    return {
        "success": True,
        "module": "QR",
        "filename": file.filename,
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "QR",
        "status": "Running"
    }