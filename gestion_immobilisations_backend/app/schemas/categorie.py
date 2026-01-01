from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.base import TimestampSchema


class CategorieBase(BaseModel):
    """Schéma de base pour Categorie"""
    code: str = Field(..., min_length=1, max_length=50)
    nom: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    parent_id: Optional[int] = None
    duree_amortissement_defaut: Optional[int] = None
    mode_amortissement_defaut: Optional[str] = Field(None, max_length=50)
    taux_degressif_defaut: Optional[Decimal] = None


class CategorieCreate(CategorieBase):
    """Schéma pour la création d'une Categorie"""
    pass


class CategorieUpdate(BaseModel):
    """Schéma pour la mise à jour d'une Categorie"""
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    nom: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    parent_id: Optional[int] = None
    duree_amortissement_defaut: Optional[int] = None
    mode_amortissement_defaut: Optional[str] = Field(None, max_length=50)
    taux_degressif_defaut: Optional[Decimal] = None


class CategorieInDB(CategorieBase, TimestampSchema):
    """Schéma Categorie en base de données"""
    id: int
    is_deleted: int
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class Categorie(CategorieInDB):
    """Schéma Categorie complet pour les réponses API"""
    pass


class CategorieSimple(BaseModel):
    """Schéma Categorie simplifié"""
    id: int
    code: str
    nom: str

    model_config = ConfigDict(from_attributes=True)
