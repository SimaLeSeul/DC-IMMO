from sqlalchemy import Column, Integer, Date, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Exercice(Base, TimestampMixin):
    __tablename__ = 'exercices'
    
    id = Column(Integer, primary_key=True, index=True)
    societe_id = Column(Integer, ForeignKey('societes.id', ondelete='CASCADE'), nullable=False)
    
    annee = Column(Integer, nullable=False, unique=True, index=True)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    
    est_cloture = Column(Boolean, default=False)
    statut = Column(String(20), default='OUVERT')  # OUVERT, CLOTURE
    
    # Relations
    societe = relationship("Societe", back_populates="exercices")
    amortissements = relationship("Amortissement", back_populates="exercice", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Exercice(annee={self.annee}, statut='{self.statut}')>"
