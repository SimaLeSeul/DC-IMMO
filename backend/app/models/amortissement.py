"""
Modèle Amortissement
"""

from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Amortissement(Base):
    """Modèle de données pour un amortissement"""
    
    __tablename__ = "amortissements"
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey("immobilisations.id"), nullable=False)
    annee = Column(Integer, nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    dotation = Column(Numeric(15, 2), nullable=False)
    cumul = Column(Numeric(15, 2), nullable=False)
    valeur_nette_comptable = Column(Numeric(15, 2), nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    immobilisation = relationship("Immobilisation", back_populates="amortissements")
