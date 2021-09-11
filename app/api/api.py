from fastapi import APIRouter

from app.api.routers import city, item, root

api_router = APIRouter()
api_router.include_router(root.router, prefix="/healt-check", tags=["Healt Check"])
api_router.include_router(item.router, prefix="/v1/items", tags=["item"])
api_router.include_router(city.router, prefix="/v1/cities", tags=["city"])
