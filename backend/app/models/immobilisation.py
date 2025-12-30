"""
Modèle Immobilisation
"""

from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Immobilisation(Base):
    """Modèle de données pour une immobilisation"""
    
    __tablename__ = "immobilisations"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    libelle = Column(String(200), nullable=False)
    date_acquisition = Column(Date, nullable=False)
    valeur_origine = Column(Numeric(15, 2), nullable=False)
    
    # Clés étrangères
    categorie_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    societe_id = Column(Integer, ForeignKey("societes.id"), nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    societe = relationship("Societe", back_populates="immobilisations")
    categorie = relationship("Categorie", back_populates="immobilisations")
    amortissements = relationship("Amortissement", back_populates="immobilisation", cascade="all, delete-orphan")
