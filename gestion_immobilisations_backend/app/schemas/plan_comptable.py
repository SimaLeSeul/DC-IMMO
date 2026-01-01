from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.base import TimestampSchema


class PlanComptableBase(BaseModel):
    """Schéma de base pour PlanComptable"""
    code: str = Field(..., min_length=1, max_length=50)
    nom: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    pays: str = Field(..., min_length=1, max_length=100)
    norme: str = Field(..., min_length=1, max_length=100)
    is_active: int = 1


class PlanComptableCreate(PlanComptableBase):
    """Schéma pour la création d'un PlanComptable"""
    pass


class PlanComptableUpdate(BaseModel):
    """Schéma pour la mise à jour d'un PlanComptable"""
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    nom: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    pays: Optional[str] = Field(None, min_length=1, max_length=100)
    norme: Optional[str] = Field(None, min_length=1, max_length=100)
    is_active: Optional[int] = None


class PlanComptableInDB(PlanComptableBase, TimestampSchema):
    """Schéma PlanComptable en base de données"""
    id: int

    model_config = ConfigDict(from_attributes=True)


class PlanComptable(PlanComptableInDB):
    """Schéma PlanComptable complet pour les réponses API"""
    pass


class PlanComptableSimple(BaseModel):
    """Schéma PlanComptable simplifié"""
    id: int
    code: str
    nom: str
    pays: str
    norme: str

    model_config = ConfigDict(from_attributes=True)
