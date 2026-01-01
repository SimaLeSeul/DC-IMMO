from sqlalchemy import Column, Integer, String, Text, Numeric, Date, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin


class Evenement(Base, TimestampMixin):
    __tablename__ = 'evenements'
    
    id = Column(Integer, primary_key=True, index=True)
    immobilisation_id = Column(Integer, ForeignKey('immobilisations.id', ondelete='CASCADE'), nullable=False, index=True)
    
    type_evenement = Column(String(50), nullable=False, index=True)
    date_evenement = Column(Date, nullable=False, index=True)
    libelle = Column(String(255))
    description = Column(Text)
    prix_vente_ht = Column(Numeric(15, 2))
    prix_vente_ttc = Column(Numeric(15, 2))
    vnc_cession = Column(Numeric(15, 2))
    plus_ou_moins_value = Column(Numeric(15, 2))
    acquereur = Column(String(255))
    ancienne_valeur = Column(Numeric(15, 2))
    nouvelle_valeur = Column(Numeric(15, 2))
    ecart_reevaluation = Column(Numeric(15, 2))
    ancienne_localisation = Column(String(255))
    nouvelle_localisation = Column(String(255))
    ancien_responsable = Column(String(255))
    nouveau_responsable = Column(String(255))
    societe_destination_id = Column(Integer, ForeignKey('societes.id'))
    donnees_supplementaires = Column(JSON)
    reference_document = Column(String(100))
    statut = Column(String(50))
    
    immobilisation = relationship("Immobilisation", back_populates="evenements")
    
    def __repr__(self):
        return f"<Evenement(id={self.id}, type='{self.type_evenement}')>"
