# backend/app/models/amortissement.py
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base, TimestampMixin


class Amortissement(Base, TimestampMixin):
    """Modèle pour les lignes d'amortissement (une par exercice)."""
    
    __tablename__ = "amortissements"

    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey("immobilisations.id", ondelete="CASCADE"), nullable=False)
    exercice = Column(Integer, nullable=False)  # Année comptable (ex: 2024)
    
    # Dates
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    
    # Montants
    valeur_origine = Column(Numeric(15, 2), nullable=False)
    base_amortissable = Column(Numeric(15, 2), nullable=False)
    taux = Column(Numeric(5, 2), nullable=False)  # Taux en %
    dotation = Column(Numeric(15, 2), nullable=False)  # Dotation de l'exercice
    cumul_amortissements = Column(Numeric(15, 2), nullable=False)
    valeur_nette_comptable = Column(Numeric(15, 2), nullable=False)
    
    # Relations
    immobilisation = relationship("Immobilisation", back_populates="amortissements")
