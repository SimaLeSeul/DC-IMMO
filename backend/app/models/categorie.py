"""
Modèle Catégorie d'immobilisation
"""

from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Categorie(Base):
    """Modèle Catégorie"""
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    libelle = Column(String(200), nullable=False)
    
    # Durée d'amortissement en années
    duree_amortissement = Column(Integer, nullable=False)
    
    # Taux d'amortissement en pourcentage
    taux_amortissement = Column(Numeric(5, 2), nullable=False)
    
    # Compte comptable
    compte_comptable = Column(String(20))
    
    # Dates de création et modification
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="categorie")
    
    def __repr__(self):
        return f"<Categorie {self.code} - {self.libelle}>"
