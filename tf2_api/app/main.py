from fastapi import FastAPI
from app.api import morphology, chat

app = FastAPI(title="AITilchi API", version="1.0")

# Подключаем маршруты
app.include_router(morphology.router, prefix="/predict", tags=["Morphology"])
app.include_router(chat.router, tags=["WebSocket Chat"])

@app.get("/")
def read_root():
    return {"message": "AITilchi API is running"}
