# Safety Voice - FastAPI 서버

## 프로젝트 구조
![image](https://github.com/user-attachments/assets/5e0e7afb-9f7b-4cb0-92c7-4388b608d515)

## 실행 방법
```bash
# 1. 프로젝트 클론
git clone https://github.com/00DDGS01/Safety_Voice-FastAPI.git
cd Safety_Voice-FastAPI

# 2. 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 서버 실행
uvicorn app.main:app --reload
```
## Swagger
http://localhost:8000/docs
