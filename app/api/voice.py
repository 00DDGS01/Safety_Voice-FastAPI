from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.voice_service import process_and_store_embedding, compare_embedding
from pydantic import BaseModel

router = APIRouter(prefix="/voice", tags=["Voice Recoginition"])

class TrainResponse(BaseModel):
    message: str

class VerifyResponse(BaseModel):
    match_score: float

@router.post("/train", response_model=TrainResponse)
async def train_voice(file: UploadFile = File(...)):
    try :
        await process_and_store_embedding(file)
        return {"message": "음성 학습 및 임베딩 저장 완료"}
    except Exception as e :
        raise HTTPException(status_code=500, detail={"error": str(e)})
    

@router.post("/verify", response_model=VerifyResponse)
async def verify_voice(file: UploadFile = File(...)):
    try:
        result = await compare_embedding(file)
        return {"match_score": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})