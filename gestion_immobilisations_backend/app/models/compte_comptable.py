from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class CompteComptable(Base, TimestampMixin):
    __tablename__ = 'comptes_comptables'
    
    id = Column(Integer, primary_key=True, index=True)
    plan_comptable_id = Column(Integer, ForeignKey('plans_comptables.id', ondelete='CASCADE'), nullable=False)
    
    numero = Column(String(20), nullable=False, index=True)
    libelle = Column(String(255), nullable=False)
    type_compte = Column(String(50), nullable=False)
    est_actif = Column(Boolean, default=True)
    description = Column(String(1000), nullable=True)
    
    # Relations
    plan_comptable = relationship("PlanComptable", back_populates="comptes")
    immobilisations = relationship("Immobilisation", back_populates="compte_comptable", lazy="dynamic")  # ← AJOUTÉ
    
    def __repr__(self):
        return f"<CompteComptable(numero='{self.numero}', libelle='{self.libelle}')>"
