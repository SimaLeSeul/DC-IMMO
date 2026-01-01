from sqlalchemy import Column, Integer, String, Numeric, Date, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Immobilisation(Base, TimestampMixin):
    __tablename__ = 'immobilisations'
    
    id = Column(Integer, primary_key=True, index=True)
    societe_id = Column(Integer, ForeignKey('societes.id', ondelete='CASCADE'), nullable=False)
    categorie_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    compte_comptable_id = Column(Integer, ForeignKey('comptes_comptables.id'), nullable=False)
    
    code = Column(String(50), unique=True, nullable=False, index=True)
    libelle = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    date_acquisition = Column(Date, nullable=False)
    date_mise_en_service = Column(Date, nullable=True)
    valeur_acquisition = Column(Numeric(15, 2), nullable=False)
    valeur_residuelle = Column(Numeric(15, 2), default=0)
    duree_amortissement = Column(Integer, nullable=False)
    mode_amortissement = Column(String(50), nullable=False)
    
    est_totalement_amorti = Column(Boolean, default=False)
    
    # Relations
    societe = relationship("Societe", back_populates="immobilisations")
    categorie = relationship("Categorie", back_populates="immobilisations")
    compte_comptable = relationship("CompteComptable", back_populates="immobilisations")
    amortissements = relationship("Amortissement", back_populates="immobilisation", cascade="all, delete-orphan", lazy="dynamic")
    dotations = relationship("Dotation", back_populates="immobilisation", cascade="all, delete-orphan", lazy="dynamic")
    documents = relationship("Document", back_populates="immobilisation", cascade="all, delete-orphan", lazy="dynamic")
    cessions = relationship("Cession", back_populates="immobilisation", cascade="all, delete-orphan")
    evenements = relationship("Evenement", back_populates="immobilisation", cascade="all, delete-orphan", lazy="dynamic")
    pieces_jointes = relationship("PieceJointe", back_populates="immobilisation", cascade="all, delete-orphan", lazy="dynamic")  # ← AJOUTÉ

    def __repr__(self):
        return f"<Immobilisation(id={self.id}, code='{self.code}', libelle='{self.libelle}')>"
