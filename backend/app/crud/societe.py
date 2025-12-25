# backend/app/crud/societe.py
from typing import Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.societe import Societe
from app.schemas.societe import SocieteCreate, SocieteUpdate


class CRUDSociete(CRUDBase[Societe, SocieteCreate, SocieteUpdate]):
    """Opérations CRUD pour les sociétés."""
    
    def get_by_code(self, db: Session, *, code: str) -> Optional[Societe]:
        """Récupère une société par son code."""
        return db.query(Societe).filter(Societe.code == code).first()
    
    def get_by_siret(self, db: Session, *, siret: str) -> Optional[Societe]:
        """Récupère une société par son SIRET."""
        return db.query(Societe).filter(Societe.siret == siret).first()
    
    def get_active(self, db: Session, *, skip: int = 0, limit: int = 100):
        """Récupère uniquement les sociétés actives."""
        return (
            db.query(Societe)
            .filter(Societe.is_active == True)
            .offset(skip)
            .limit(limit)
            .all()
        )


# Instance unique
societe = CRUDSociete(Societe)
