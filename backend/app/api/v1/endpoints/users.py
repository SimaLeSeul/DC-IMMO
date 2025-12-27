"""
Endpoints utilisateurs
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_users():
    return {"message": "Liste utilisateurs - À implémenter"}

@router.get("/me")
async def get_current_user():
    return {"message": "Utilisateur courant - À implémenter"}
