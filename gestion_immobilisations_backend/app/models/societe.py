from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Societe(Base, TimestampMixin):
    __tablename__ = 'societes'
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    raison_sociale = Column(String(255), nullable=False)
    siret = Column(String(14), unique=True, nullable=True)
    
    adresse = Column(String(255), nullable=True)
    code_postal = Column(String(10), nullable=True)
    ville = Column(String(100), nullable=True)
    pays = Column(String(100), default="France")
    
    telephone = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
    
    is_active = Column(Boolean, default=True)
    
    # Relations
    users = relationship("User", back_populates="societe", cascade="all, delete-orphan")
    plans_comptables = relationship("PlanComptable", back_populates="societe", cascade="all, delete-orphan")
    categories = relationship("Categorie", back_populates="societe", cascade="all, delete-orphan")
    exercices = relationship("Exercice", back_populates="societe", cascade="all, delete-orphan")
    immobilisations = relationship("Immobilisation", back_populates="societe", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Societe(id={self.id}, code='{self.code}', raison_sociale='{self.raison_sociale}')>"
