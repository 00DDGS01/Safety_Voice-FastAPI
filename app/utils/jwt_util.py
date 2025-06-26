from jose import jwt 
from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = "HS256"

def extract_user_id_from_jwt(token: str) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return str(payload.get("userId")or payload.get("sub"))
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid JWT token")