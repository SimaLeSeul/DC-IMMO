from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin, SoftDeleteMixin


class PieceJointe(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'pieces_jointes'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False, index=True)
    
    nom_fichier = Column(String(255), nullable=False)
    nom_original = Column(String(255))
    chemin_fichier = Column(String(500), nullable=False)
    type_mime = Column(String(100))
    taille = Column(BigInteger)
    type_document = Column(String(50))
    description = Column(String(500))
    
    immobilisation = relationship("Immobilisation", back_populates="pieces_jointes")
    
    def __repr__(self):
        return f"<PieceJointe(id={self.id}, nom='{self.nom_fichier}')>"
