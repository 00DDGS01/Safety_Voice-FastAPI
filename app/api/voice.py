from fastapi import APIRouter, UploadFile, File, HTTPException, Header, Depends
from app.services.voice_service import process_and_store_embedding, compare_embedding
from app.services.notify_spring import notify_spring_voice_trained
from app.utils.jwt_util import extract_user_id_from_jwt
from pydantic import BaseModel

router = APIRouter(prefix="/voice", tags=["Voice Recoginition"])

class TrainResponse(BaseModel):
    message: str

class VerifyResponse(BaseModel):
    match_score: float

# JWT 추출 함수
async def get_jwt_token(authorization: str = Header(...)):
    print("Authorization header:", authorization)  
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    return authorization.replace("Bearer ", "")

@router.post("/train", response_model=TrainResponse)
async def train_voice(
    file: UploadFile = File(...),
    user_jwt: str = Depends(get_jwt_token)
):
    print(f"[train_voice] file: {file.filename}")
    try :
        user_id = extract_user_id_from_jwt(user_jwt)
        await process_and_store_embedding(file, user_id)
        await notify_spring_voice_trained(user_jwt)
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