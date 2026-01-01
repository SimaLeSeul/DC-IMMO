from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.base import TimestampSchema


class CompteComptableBase(BaseModel):
    """Schéma de base pour CompteComptable"""
    plan_comptable_id: int
    numero: str = Field(..., min_length=1, max_length=20)
    libelle: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    type_compte: str = Field(..., min_length=1, max_length=50)
    classe: Optional[str] = Field(None, max_length=10)
    is_active: int = 1


class CompteComptableCreate(CompteComptableBase):
    """Schéma pour la création d'un CompteComptable"""
    pass


class CompteComptableUpdate(BaseModel):
    """Schéma pour la mise à jour d'un CompteComptable"""
    numero: Optional[str] = Field(None, min_length=1, max_length=20)
    libelle: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    type_compte: Optional[str] = Field(None, min_length=1, max_length=50)
    classe: Optional[str] = Field(None, max_length=10)
    is_active: Optional[int] = None


class CompteComptableInDB(CompteComptableBase, TimestampSchema):
    """Schéma CompteComptable en base de données"""
    id: int

    model_config = ConfigDict(from_attributes=True)


class CompteComptable(CompteComptableInDB):
    """Schéma CompteComptable complet pour les réponses API"""
    pass


class CompteComptableSimple(BaseModel):
    """Schéma CompteComptable simplifié"""
    id: int
    numero: str
    libelle: str
    type_compte: str

    model_config = ConfigDict(from_attributes=True)
