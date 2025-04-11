from fastapi import FastAPI
from app.database import init_db
from app.routes import notify


app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(notify.router)

@app.get("/ping")
async def ping():
    return {"message": "notification service is alive!"}
