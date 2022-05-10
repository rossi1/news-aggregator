from fastapi import APIRouter

from app.api.endpoints import news

api_router = APIRouter()
api_router.include_router(news.router, prefix="/news", tags=["news"])
