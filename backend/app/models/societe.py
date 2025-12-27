"""
Modèle Société
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class Societe(Base):
    """Modèle Société"""
    __tablename__ = "societes"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, index=True, nullable=False)
    raison_sociale = Column(String(200), nullable=False)
    siret = Column(String(14), unique=True)
    adresse = Column(String(500))
    code_postal = Column(String(10))
    ville = Column(String(100))
    pays = Column(String(30))
    
    # Dates de création et modification
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    immobilisations = relationship("Immobilisation", back_populates="societe")
    
    def __repr__(self):
        return f"<Societe {self.code} - {self.raison_sociale}>"
