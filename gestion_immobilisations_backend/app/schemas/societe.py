from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from app.schemas.base import TimestampSchema


class SocieteBase(BaseModel):
    """Schéma de base pour Societe"""
    code: str = Field(..., min_length=1, max_length=50)
    nom: str = Field(..., min_length=1, max_length=255)
    raison_sociale: str = Field(..., min_length=1, max_length=255)
    
    # Informations légales
    siret: Optional[str] = Field(None, max_length=14)
    siren: Optional[str] = Field(None, max_length=9)
    tva_intracommunautaire: Optional[str] = Field(None, max_length=13)
    forme_juridique: Optional[str] = Field(None, max_length=100)
    capital: Optional[str] = Field(None, max_length=100)
    
    # Adresse
    adresse: Optional[str] = None
    code_postal: Optional[str] = Field(None, max_length=10)
    ville: Optional[str] = Field(None, max_length=100)
    pays: str = Field(default='France', max_length=100)
    
    # Contacts
    telephone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    site_web: Optional[str] = Field(None, max_length=255)
    
    # Paramètres comptables
    devise: str = Field(default='EUR', max_length=3)
    langue: str = Field(default='fr', pattern='^(fr|en)$')
    date_debut_exercice: Optional[date] = None
    date_fin_exercice: Optional[date] = None
    
    # Plan comptable
    plan_comptable_id: Optional[int] = None


class SocieteCreate(SocieteBase):
    """Schéma pour la création d'une Societe"""
    pass


class SocieteUpdate(BaseModel):
    """Schéma pour la mise à jour d'une Societe"""
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    nom: Optional[str] = Field(None, min_length=1, max_length=255)
    raison_sociale: Optional[str] = Field(None, min_length=1, max_length=255)
    siret: Optional[str] = Field(None, max_length=14)
    siren: Optional[str] = Field(None, max_length=9)
    tva_intracommunautaire: Optional[str] = Field(None, max_length=13)
    forme_juridique: Optional[str] = Field(None, max_length=100)
    capital: Optional[str] = Field(None, max_length=100)
    adresse: Optional[str] = None
    code_postal: Optional[str] = Field(None, max_length=10)
    ville: Optional[str] = Field(None, max_length=100)
    pays: Optional[str] = Field(None, max_length=100)
    telephone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    site_web: Optional[str] = Field(None, max_length=255)
    devise: Optional[str] = Field(None, max_length=3)
    langue: Optional[str] = Field(None, pattern='^(fr|en)$')
    date_debut_exercice: Optional[date] = None
    date_fin_exercice: Optional[date] = None
    plan_comptable_id: Optional[int] = None


class SocieteInDB(SocieteBase, TimestampSchema):
    """Schéma Societe en base de données"""
    id: int
    is_deleted: int
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class Societe(SocieteInDB):
    """Schéma Societe complet pour les réponses API"""
    pass


class SocieteSimple(BaseModel):
    """Schéma Societe simplifié"""
    id: int
    code: str
    nom: str
    raison_sociale: str

    model_config = ConfigDict(from_attributes=True)
