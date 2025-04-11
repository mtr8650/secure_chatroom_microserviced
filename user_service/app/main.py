from fastapi import FastAPI
from app.database import init_db
from app.routes import profile

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(profile.router)

@app.get("/ping")
async def ping():
    return {"message": "user service is alive!"}