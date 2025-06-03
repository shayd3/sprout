from fastapi import APIRouter

from . import weather

api_router = APIRouter()

api_router.include_router(
    weather.router,
    prefix="/weather",
    tags=["Weather"]
)
