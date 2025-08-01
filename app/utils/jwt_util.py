from jose import jwt 
from fastapi import Header, HTTPException
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dotenv_path)

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = "HS256"

print(f"Loaded JWT_SECRET from {dotenv_path}: {JWT_SECRET is not None}")

def extract_user_id_from_jwt(token: str) -> str:
    if not JWT_SECRET:
        raise RuntimeError("JWT_SECRET is not set. Check your .env file path.")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return str(payload.get("userId")or payload.get("sub"))
    except jwt.JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid JWT token")