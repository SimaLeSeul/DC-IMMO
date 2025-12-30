"""
CRUD operations pour les sociétés
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.societe import Societe
from app.schemas.societe import SocieteCreate, SocieteUpdate


class CRUDSociete:
    """Opérations CRUD pour les sociétés"""
    
    def get(self, db: Session, societe_id: int) -> Optional[Societe]:
        """Récupérer une société par son ID"""
        return db.query(Societe).filter(Societe.id == societe_id).first()
    
    def get_by_code(self, db: Session, code: str) -> Optional[Societe]:
        """Récupérer une société par son code"""
        return db.query(Societe).filter(Societe.code == code).first()
    
    def get_multi(
        self, 
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Societe]:
        """Récupérer plusieurs sociétés avec pagination"""
        return db.query(Societe).offset(skip).limit(limit).all()
    
    def create(self, db: Session, societe_in: SocieteCreate) -> Societe:
        """Créer une nouvelle société"""
        db_societe = Societe(**societe_in.model_dump())
        db.add(db_societe)
        db.commit()
        db.refresh(db_societe)
        return db_societe
    
    def update(
        self, 
        db: Session, 
        societe_id: int, 
        societe_in: SocieteUpdate
    ) -> Optional[Societe]:
        """Mettre à jour une société"""
        db_societe = self.get(db, societe_id)
        if not db_societe:
            return None
        
        # Mise à jour des champs fournis
        update_data = societe_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_societe, field, value)
        
        db.commit()
        db.refresh(db_societe)
        return db_societe
    
    def delete(self, db: Session, societe_id: int) -> bool:
        """Supprimer une société"""
        db_societe = self.get(db, societe_id)
        if not db_societe:
            return False
        
        db.delete(db_societe)
        db.commit()
        return True


# Instance unique du CRUD
crud_societe = CRUDSociete()
