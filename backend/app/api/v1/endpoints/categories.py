"""
Endpoints pour les catégories
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.categorie import CategorieCreate, CategorieUpdate, CategorieResponse
from app.crud.categorie import categorie

router = APIRouter()


@router.get("/", response_model=List[CategorieResponse])
def list_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Récupérer toutes les catégories
    """
    categories = categorie.get_multi(db, skip=skip, limit=limit)
    return categories


@router.get("/{categorie_id}", response_model=CategorieResponse)
def get_categorie(
    categorie_id: int,
    db: Session = Depends(get_db)
):
    """
    Récupérer une catégorie par ID
    """
    db_categorie = categorie.get(db, id=categorie_id)
    if not db_categorie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Catégorie non trouvée"
        )
    return db_categorie


@router.post("/", response_model=CategorieResponse, status_code=status.HTTP_201_CREATED)
def create_categorie(
    categorie_in: CategorieCreate,
    db: Session = Depends(get_db)
):
    """
    Créer une nouvelle catégorie
    """
    # Vérifier si le code existe déjà
    existing = categorie.get_by_code(db, code=categorie_in.code)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Une catégorie avec ce code existe déjà"
        )
    
    return categorie.create(db, obj_in=categorie_in)


@router.put("/{categorie_id}", response_model=CategorieResponse)
def update_categorie(
    categorie_id: int,
    categorie_in: CategorieUpdate,
    db: Session = Depends(get_db)
):
    """
    Mettre à jour une catégorie
    """
    db_categorie = categorie.get(db, id=categorie_id)
    if not db_categorie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Catégorie non trouvée"
        )
    
    # Vérifier si le nouveau code existe déjà (si changé)
    if categorie_in.code and categorie_in.code != db_categorie.code:
        existing = categorie.get_by_code(db, code=categorie_in.code)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Une catégorie avec ce code existe déjà"
            )
    
    return categorie.update(db, db_obj=db_categorie, obj_in=categorie_in)


@router.delete("/{categorie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categorie(
    categorie_id: int,
    db: Session = Depends(get_db)
):
    """
    Supprimer une catégorie
    """
    db_categorie = categorie.get(db, id=categorie_id)
    if not db_categorie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Catégorie non trouvée"
        )
    
    categorie.remove(db, id=categorie_id)
    return None
