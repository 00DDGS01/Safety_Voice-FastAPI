from typing import Union
from fastapi import FastAPI
from app.api.voice import router as voice_router
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(voice_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

bearer_scheme = HTTPBearer()

# Swagger OpenAPI 문서에 보안 스키마 반영
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Safety Voice API",
        version="1.0.0",
        description="FastAPI backend for voice processing",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi