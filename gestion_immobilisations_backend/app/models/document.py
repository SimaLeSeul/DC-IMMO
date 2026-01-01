from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Document(Base, TimestampMixin):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False)
    nom_fichier = Column(String(255), nullable=False)
    type_document = Column(String(50), nullable=True)
    chemin_fichier = Column(String(500), nullable=False)
    taille = Column(Integer, nullable=True)  # En octets
    
    # Relations
    immobilisation = relationship("Immobilisation", back_populates="documents")
    
    def __repr__(self):
        return f"<Document(id={self.id}, nom='{self.nom_fichier}')>"
