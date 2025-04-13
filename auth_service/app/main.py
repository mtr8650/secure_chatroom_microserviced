from fastapi import FastAPI
from app.database import init_db
from app.routes import auth

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(auth.router)

@app.get("/ping")
async def ping():
    return {"message": "auth service is alive!"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
