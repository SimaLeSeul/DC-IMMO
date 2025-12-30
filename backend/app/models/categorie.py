"""
Modèle Catégorie
"""

from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Categorie(Base):
    """Modèle de données pour une catégorie d'immobilisation"""
    
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    libelle = Column(String(200), nullable=False)
    duree_amortissement = Column(Integer, nullable=False)
    taux_amortissement = Column(Numeric(5, 2), nullable=False)
    compte_comptable = Column(String(20))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="categorie")
