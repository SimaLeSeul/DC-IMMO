"""
Router principal API v1
"""

from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, categories, societes, immobilisations

api_router = APIRouter()

# Inclure les routers des endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["Authentification"])
api_router.include_router(users.router, prefix="/users", tags=["Utilisateurs"])
api_router.include_router(categories.router, prefix="/categories", tags=["Catégories"])
api_router.include_router(societes.router, prefix="/societes", tags=["Sociétés"])
api_router.include_router(immobilisations.router, prefix="/immobilisations", tags=["Immobilisations"])
