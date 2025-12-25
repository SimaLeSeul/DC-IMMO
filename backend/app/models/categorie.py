# backend/app/models/categorie.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base, TimestampMixin


class Categorie(Base, TimestampMixin):
    """Modèle pour les catégories d'immobilisations."""
    
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    libelle = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    taux_amortissement = Column(Integer, nullable=True)  # Taux par défaut en %
    is_active = Column(Boolean, default=True)
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="categorie")
