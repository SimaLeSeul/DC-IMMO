from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Amortissement(Base, TimestampMixin):
    __tablename__ = 'amortissements'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False)
    exercice_id = Column(Integer, ForeignKey('exercices.id', ondelete='CASCADE'), nullable=False)
    
    annee = Column(Integer, nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    
    dotation = Column(Numeric(15, 2), nullable=False)
    amortissement_cumule = Column(Numeric(15, 2), nullable=False)
    valeur_nette_comptable = Column(Numeric(15, 2), nullable=False)
    
    # Relations
    immobilisation = relationship("Immobilisation", back_populates="amortissements")
    exercice = relationship("Exercice", back_populates="amortissements")
    dotations = relationship("Dotation", back_populates="amortissement", cascade="all, delete-orphan", lazy="dynamic")  # ← AJOUTÉ
    
    def __repr__(self):
        return f"<Amortissement(immobilisation_id={self.immobilisation_id}, annee={self.annee})>"
