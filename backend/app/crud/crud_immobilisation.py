# backend/app/crud/immobilisation.py
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date

from app.crud.base import CRUDBase
from app.models.immobilisation import Immobilisation
from app.schemas.immobilisation import ImmobilisationCreate, ImmobilisationUpdate


class CRUDImmobilisation(CRUDBase[Immobilisation, ImmobilisationCreate, ImmobilisationUpdate]):
    """Opérations CRUD pour les immobilisations."""
    
    def get_by_societe(
        self, 
        db: Session, 
        *, 
        societe_id: int,
        skip: int = 0,
        limit: int = 100
    ) -> List[Immobilisation]:
        """Récupère les immobilisations d'une société."""
        return (
            db.query(Immobilisation)
            .filter(Immobilisation.societe_id == societe_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_code(self, db: Session, *, code: str) -> Optional[Immobilisation]:
        """Récupère une immobilisation par son code."""
        return db.query(Immobilisation).filter(Immobilisation.code == code).first()
    
    def get_active_immobilisations(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100
    ) -> List[Immobilisation]:
        """Récupère les immobilisations non cédées."""
        return (
            db.query(Immobilisation)
            .filter(Immobilisation.date_cession.is_(None))
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_date_range(
        self,
        db: Session,
        *,
        date_debut: date,
        date_fin: date,
        skip: int = 0,
        limit: int = 100
    ) -> List[Immobilisation]:
        """Récupère les immobilisations acquises dans une période."""
        return (
            db.query(Immobilisation)
            .filter(
                Immobilisation.date_acquisition >= date_debut,
                Immobilisation.date_acquisition <= date_fin
            )
            .offset(skip)
            .limit(limit)
            .all()
        )


# Instance unique
crud_immobilisation = CRUDImmobilisation(Immobilisation)
