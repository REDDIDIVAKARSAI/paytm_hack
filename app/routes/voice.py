from fastapi import APIRouter, UploadFile
import shutil

from app.services.speech import speech_to_text
from app.services.parser import parse_text

router = APIRouter()

@router.post("/voice-input")
async def voice_input(file: UploadFile):
    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = speech_to_text(path)
    parsed = parse_text(text)

    return {"text": text, "parsed": parsed}