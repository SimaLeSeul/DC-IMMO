from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_societes():
    return {"message": "Liste des sociétés"}
