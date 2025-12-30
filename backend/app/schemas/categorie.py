"""
Schémas Pydantic pour les catégories
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CategorieBase(BaseModel):
    """Schéma de base"""
    code: str = Field(..., max_length=20, description="Code unique de la catégorie")
    libelle: str = Field(..., max_length=200, description="Libellé de la catégorie")
    duree_amortissement: int = Field(..., gt=0, description="Durée en années")
    taux_amortissement: float = Field(..., gt=0, le=100, description="Taux en %")
    compte_comptable: Optional[str] = Field(None, max_length=20)


class CategorieCreate(CategorieBase):
    """Schéma pour la création"""
    pass


class CategorieUpdate(BaseModel):
    """Schéma pour la mise à jour (tous les champs optionnels)"""
    code: Optional[str] = Field(None, max_length=20)
    libelle: Optional[str] = Field(None, max_length=200)
    duree_amortissement: Optional[int] = Field(None, gt=0)
    taux_amortissement: Optional[float] = Field(None, gt=0, le=100)
    compte_comptable: Optional[str] = Field(None, max_length=20)


class CategorieInDB(CategorieBase):
    """Schéma pour la lecture depuis la DB"""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class CategorieResponse(CategorieInDB):
    """Schéma pour les réponses API"""
    pass
