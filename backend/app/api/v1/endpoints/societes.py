"""
Endpoints pour les sociétés
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.societe import SocieteCreate, SocieteUpdate, SocieteResponse
from app.crud.societe import societe

router = APIRouter()


@router.get("/", response_model=List[SocieteResponse])
def list_societes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Récupérer toutes les sociétés
    """
    societes = societe.get_multi(db, skip=skip, limit=limit)
    return societes


@router.get("/{societe_id}", response_model=SocieteResponse)
def get_societe(
    societe_id: int,
    db: Session = Depends(get_db)
):
    """
    Récupérer une société par ID
    """
    db_societe = societe.get(db, id=societe_id)
    if not db_societe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Société non trouvée"
        )
    return db_societe


@router.post("/", response_model=SocieteResponse, status_code=status.HTTP_201_CREATED)
def create_societe(
    societe_in: SocieteCreate,
    db: Session = Depends(get_db)
):
    """
    Créer une nouvelle société
    """
    # Vérifier si le code existe déjà
    existing = societe.get_by_code(db, code=societe_in.code)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Une société avec ce code existe déjà"
        )
    
    return societe.create(db, obj_in=societe_in)


@router.put("/{societe_id}", response_model=SocieteResponse)
def update_societe(
    societe_id: int,
    societe_in: SocieteUpdate,
    db: Session = Depends(get_db)
):
    """
    Mettre à jour une société
    """
    db_societe = societe.get(db, id=societe_id)
    if not db_societe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Société non trouvée"
        )
    
    # Vérifier si le nouveau code existe déjà (si changé)
    if societe_in.code and societe_in.code != db_societe.code:
        existing = societe.get_by_code(db, code=societe_in.code)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Une société avec ce code existe déjà"
            )
    
    return societe.update(db, db_obj=db_societe, obj_in=societe_in)


@router.delete("/{societe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_societe(
    societe_id: int,
    db: Session = Depends(get_db)
):
    """
    Supprimer une société
    """
    db_societe = societe.get(db, id=societe_id)
    if not db_societe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Société non trouvée"
        )
    
    societe.remove(db, id=societe_id)
    return None
