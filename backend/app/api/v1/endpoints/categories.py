"""
Endpoints catégories
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_categories():
    return {"message": "Liste catégories - À implémenter"}

@router.post("/")
async def create_category():
    return {"message": "Création catégorie - À implémenter"}
