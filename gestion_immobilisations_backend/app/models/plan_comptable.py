from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class PlanComptable(Base, TimestampMixin):
    __tablename__ = 'plans_comptables'
    
    id = Column(Integer, primary_key=True, index=True)
    societe_id = Column(Integer, ForeignKey('societes.id', ondelete='CASCADE'), nullable=False, index=True)
    
    code = Column(String(50), nullable=False, index=True)
    libelle = Column(String(255), nullable=False)  # ✅ Ajouté
    nom = Column(String(255), nullable=False)
    description = Column(Text)
    pays = Column(String(100))
    devise = Column(String(10))
    is_actif = Column(Boolean, default=True, nullable=False)
    
    societe = relationship("Societe", back_populates="plans_comptables")
    comptes = relationship("CompteComptable", back_populates="plan_comptable", cascade="all, delete-orphan", lazy="dynamic")
    
    def __repr__(self):
        return f"<PlanComptable(id={self.id}, code='{self.code}', nom='{self.nom}')>"
