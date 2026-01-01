from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Categorie(Base, TimestampMixin):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    societe_id = Column(Integer, ForeignKey('societes.id', ondelete='CASCADE'), nullable=False)
    
    code = Column(String(50), nullable=False)
    libelle = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # Relations
    societe = relationship("Societe", back_populates="categories")
    immobilisations = relationship("Immobilisation", back_populates="categorie", lazy="dynamic")
    
    def __repr__(self):
        return f"<Categorie(id={self.id}, code='{self.code}', libelle='{self.libelle}')>"
