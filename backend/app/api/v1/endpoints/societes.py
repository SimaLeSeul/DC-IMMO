"""
Endpoints sociétés
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_societes():
    return {"message": "Liste sociétés - À implémenter"}

@router.post("/")
async def create_societe():
    return {"message": "Création société - À implémenter"}
