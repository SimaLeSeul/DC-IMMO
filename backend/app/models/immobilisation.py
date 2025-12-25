# backend/app/models/immobilisation.py
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base, TimestampMixin


class Immobilisation(Base, TimestampMixin):
    """Modèle pour les immobilisations."""
    
    __tablename__ = "immobilisations"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    libelle = Column(String(200), nullable=False)
    
    # Relations
    societe_id = Column(Integer, ForeignKey("societes.id"), nullable=False)
    categorie_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Valeurs
    valeur_acquisition = Column(Numeric(15, 2), nullable=False)
    valeur_residuelle = Column(Numeric(15, 2), default=0)
    
    # Dates
    date_acquisition = Column(Date, nullable=False)
    date_mise_en_service = Column(Date, nullable=True)
    
    # Amortissement
    duree_amortissement = Column(Integer, nullable=False)  # En années
    
    is_active = Column(Boolean, default=True)
    
    # Relations
    societe = relationship("Societe", back_populates="immobilisations")
    categorie = relationship("Categorie", back_populates="immobilisations")
    amortissements = relationship("Amortissement", back_populates="immobilisation", cascade="all, delete-orphan")  # ← CORRIGÉ
