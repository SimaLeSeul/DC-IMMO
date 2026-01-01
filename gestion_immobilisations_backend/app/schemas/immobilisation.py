from typing import Optional
from datetime import date, datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.base import TimestampSchema


class ImmobilisationBase(BaseModel):
    """Schéma de base pour Immobilisation"""
    numero: str = Field(..., min_length=1, max_length=50)
    libelle: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    
    societe_id: int
    categorie_id: Optional[int] = None
    
    date_acquisition: date
    date_mise_en_service: date
    
    valeur_origine_ht: Decimal = Field(..., ge=0)
    valeur_origine_ttc: Optional[Decimal] = Field(None, ge=0)
    tva: Optional[Decimal] = Field(None, ge=0)
    valeur_residuelle: Decimal = Field(default=Decimal('0'), ge=0)
    
    fournisseur: Optional[str] = Field(None, max_length=255)
    numero_facture: Optional[str] = Field(None, max_length=100)
    date_facture: Optional[date] = None
    
    localisation: Optional[str] = Field(None, max_length=255)
    code_barre: Optional[str] = Field(None, max_length=100)
    numero_serie: Optional[str] = Field(None, max_length=100)
    
    responsable: Optional[str] = Field(None, max_length=255)
    departement: Optional[str] = Field(None, max_length=100)
    
    compte_actif_id: Optional[int] = None
    compte_amortissement_id: Optional[int] = None
    compte_dotation_id: Optional[int] = None
    
    code_analytique: Optional[str] = Field(None, max_length=50)
    projet: Optional[str] = Field(None, max_length=255)
    
    statut: str = Field(default='EN_SERVICE', max_length=50)
    
    date_fin_garantie: Optional[date] = None
    duree_garantie_mois: Optional[int] = None


class ImmobilisationCreate(ImmobilisationBase):
    """Schéma pour la création d'une Immobilisation"""
    pass


class ImmobilisationUpdate(BaseModel):
    """Schéma pour la mise à jour d'une Immobilisation"""
    numero: Optional[str] = Field(None, min_length=1, max_length=50)
    libelle: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    categorie_id: Optional[int] = None
    date_acquisition: Optional[date] = None
    date_mise_en_service: Optional[date] = None
    valeur_origine_ht: Optional[Decimal] = Field(None, ge=0)
    valeur_origine_ttc: Optional[Decimal] = Field(None, ge=0)
    tva: Optional[Decimal] = Field(None, ge=0)
    valeur_residuelle: Optional[Decimal] = Field(None, ge=0)
    fournisseur: Optional[str] = Field(None, max_length=255)
    numero_facture: Optional[str] = Field(None, max_length=100)
    date_facture: Optional[date] = None
    localisation: Optional[str] = Field(None, max_length=255)
    code_barre: Optional[str] = Field(None, max_length=100)
    numero_serie: Optional[str] = Field(None, max_length=100)
    responsable: Optional[str] = Field(None, max_length=255)
    departement: Optional[str] = Field(None, max_length=100)
    compte_actif_id: Optional[int] = None
    compte_amortissement_id: Optional[int] = None
    compte_dotation_id: Optional[int] = None
    code_analytique: Optional[str] = Field(None, max_length=50)
    projet: Optional[str] = Field(None, max_length=255)
    statut: Optional[str] = Field(None, max_length=50)
    date_fin_garantie: Optional[date] = None
    duree_garantie_mois: Optional[int] = None


class ImmobilisationInDB(ImmobilisationBase, TimestampSchema):
    """Schéma Immobilisation en base de données"""
    id: int
    is_deleted: int
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class Immobilisation(ImmobilisationInDB):
    """Schéma Immobilisation complet pour les réponses API"""
    pass


class ImmobilisationSimple(BaseModel):
    """Schéma Immobilisation simplifié"""
    id: int
    numero: str
    libelle: str
    valeur_origine_ht: Decimal
    statut: str

    model_config = ConfigDict(from_attributes=True)
