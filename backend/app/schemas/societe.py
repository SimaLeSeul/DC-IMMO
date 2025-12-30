"""
Schémas Pydantic pour les sociétés
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class SocieteBase(BaseModel):
    """Schéma de base pour une société"""
    code: str = Field(..., min_length=1, max_length=50, description="Code unique de la société")
    raison_sociale: str = Field(..., min_length=1, max_length=255, description="Raison sociale")
    siret: Optional[str] = Field(None, max_length=14, description="Numéro SIRET")
    adresse: Optional[str] = Field(None, max_length=255, description="Adresse")
    code_postal: Optional[str] = Field(None, max_length=10, description="Code postal")
    ville: Optional[str] = Field(None, max_length=100, description="Ville")
    pays: Optional[str] = Field(default="France", max_length=100, description="Pays")
    forme_juridique: Optional[str] = Field(None, max_length=50, description="Forme juridique")


class SocieteCreate(SocieteBase):
    """Schéma pour créer une société"""
    pass


class SocieteUpdate(BaseModel):
    """Schéma pour mettre à jour une société"""
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    raison_sociale: Optional[str] = Field(None, min_length=1, max_length=255)
    siret: Optional[str] = Field(None, max_length=14)
    adresse: Optional[str] = Field(None, max_length=255)
    code_postal: Optional[str] = Field(None, max_length=10)
    ville: Optional[str] = Field(None, max_length=100)
    pays: Optional[str] = Field(None, max_length=100)
    forme_juridique: Optional[str] = Field(None, max_length=50)


class SocieteInDB(SocieteBase):
    """Schéma pour une société en base de données"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class SocieteResponse(SocieteInDB):
    """Schéma de réponse pour une société"""
    pass
