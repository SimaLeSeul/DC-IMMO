"""
Routeur principal API V1
"""

from fastapi import APIRouter
from app.api.v1.endpoints import categories, societes

api_router = APIRouter()

# Inclusion des routes
api_router.include_router(
    categories.router,
    prefix="/categories",
    tags=["Catégories"]
)

api_router.include_router(
    societes.router,
    prefix="/societes",
    tags=["Sociétés"]
)
