# backend/app/models/societe.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base, TimestampMixin


class Societe(Base, TimestampMixin):
    """Modèle pour les sociétés."""
    
    __tablename__ = "societes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    raison_sociale = Column(String(200), nullable=False)
    siret = Column(String(14), unique=True, nullable=True)
    
    # Coordonnées
    adresse = Column(String(500), nullable=True)
    code_postal = Column(String(10), nullable=True)
    ville = Column(String(100), nullable=True)
    pays = Column(String(100), default="France")
    telephone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    
    is_active = Column(Boolean, default=True)
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="societe")  # ← AJOUTÉ
