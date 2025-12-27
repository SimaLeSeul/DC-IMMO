"""
Endpoints d'authentification
"""

from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"message": "Login endpoint - À implémenter"}

@router.post("/logout")
async def logout():
    return {"message": "Logout endpoint - À implémenter"}
