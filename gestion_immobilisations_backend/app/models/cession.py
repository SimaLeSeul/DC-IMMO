from sqlalchemy import Column, Integer, Numeric, Date, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Cession(Base, TimestampMixin):
    __tablename__ = 'cessions'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False)
    
    date_cession = Column(Date, nullable=False)
    prix_cession = Column(Numeric(15, 2), nullable=False)
    
    motif = Column(String(50), nullable=True)  # VENTE, MISE_AU_REBUT, DON, etc.
    acquereur = Column(String(255), nullable=True)
    observations = Column(Text, nullable=True)
    
    # Calculs automatiques
    valeur_nette_comptable = Column(Numeric(15, 2), nullable=False)
    plus_ou_moins_value = Column(Numeric(15, 2), nullable=False)
    
    # Relations
    immobilisation = relationship("Immobilisation", back_populates="cessions")
    
    def __repr__(self):
        return f"<Cession(id={self.id}, immobilisation_id={self.immobilisation_id}, date={self.date_cession})>"
