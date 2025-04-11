from fastapi import FastAPI
from app.database import init_db
from app.routes import message

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(message.router)

@app.get("/ping")
async def ping():
    return {"message": "chat service is alive!"}
