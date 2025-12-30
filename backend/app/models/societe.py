"""
Modèle Société
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Societe(Base):
    """Modèle de données pour une société"""
    
    __tablename__ = "societes"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    raison_sociale = Column(String(255), nullable=False)
    siret = Column(String(14), unique=True, index=True)
    adresse = Column(String(255))
    code_postal = Column(String(10))
    ville = Column(String(100))
    forme_juridique = Column(String(50))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="societe", cascade="all, delete-orphan")
