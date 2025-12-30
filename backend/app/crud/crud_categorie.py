"""
Opérations CRUD pour les catégories
"""

from typing import Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.categorie import Categorie
from app.schemas.categorie import CategorieCreate, CategorieUpdate


class CRUDCategorie(CRUDBase[Categorie, CategorieCreate, CategorieUpdate]):
    """CRUD pour les catégories"""
    
    def get_by_code(self, db: Session, *, code: str) -> Optional[Categorie]:
        """Récupérer une catégorie par son code"""
        return db.query(Categorie).filter(Categorie.code == code).first()


crud_categorie = CRUDCategorie(Categorie)
