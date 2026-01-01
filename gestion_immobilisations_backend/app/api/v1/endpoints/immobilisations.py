from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_immobilisations():
    return {"message": "Liste des immobilisations"}
