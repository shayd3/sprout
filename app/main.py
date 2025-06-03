from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI

from api.v1.api import api_router

load_dotenv()

app = FastAPI(
    title="Sprout",
    description="A comprehensive indoor and outdoor plant watering tracker and predictor that helps you keep your plants healthy and thriving",
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Sprout API is running!"}
