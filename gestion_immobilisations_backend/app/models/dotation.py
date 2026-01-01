from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Dotation(Base, TimestampMixin):
    __tablename__ = 'dotations'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False, index=True)
    amortissement_id = Column(Integer, ForeignKey('amortissements.id', ondelete='CASCADE'), index=True)
    
    exercice = Column(Integer, nullable=False, index=True)
    periode = Column(Integer)
    date_dotation = Column(Date, nullable=False)
    montant = Column(Numeric(15, 2), nullable=False)
    cumul_anterieur = Column(Numeric(15, 2))
    cumul_apres = Column(Numeric(15, 2))
    vnc_apres = Column(Numeric(15, 2))
    type_dotation = Column(String(50))
    statut = Column(String(50))
    date_validation = Column(Date)
    date_comptabilisation = Column(Date)
    numero_piece = Column(String(50))
    commentaire = Column(String(500))
    
    immobilisation = relationship("Immobilisation", back_populates="dotations")
    amortissement = relationship("Amortissement", back_populates="dotations")
    
    def __repr__(self):
        return f"<Dotation(id={self.id}, exercice={self.exercice}, montant={self.montant})>"
