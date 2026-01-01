from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, societes, immobilisations

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(societes.router, prefix="/societes", tags=["Sociétés"])
api_router.include_router(immobilisations.router, prefix="/immobilisations", tags=["Immobilisations"])
