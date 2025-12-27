"""
Endpoints immobilisations
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_immobilisations():
    return {"message": "Liste immobilisations - À implémenter"}

@router.post("/")
async def create_immobilisation():
    return {"message": "Création immobilisation - À implémenter"}
