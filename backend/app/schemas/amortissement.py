"""
Schémas Pydantic pour les amortissements
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class AmortissementBase(BaseModel):
    """Schéma de base pour un amortissement"""
    exercice: int = Field(..., ge=2000, le=2100, description="Année d'exercice")
    date_debut: date = Field(..., description="Date de début de période")
    date_fin: date = Field(..., description="Date de fin de période")
    dotation: Decimal = Field(..., ge=0, description="Montant de la dotation")
    amortissement_cumule: Decimal = Field(..., ge=0, description="Amortissement cumulé")
    valeur_nette_comptable: Decimal = Field(..., ge=0, description="Valeur nette comptable")
    
    # Clé étrangère
    immobilisation_id: int = Field(..., description="ID de l'immobilisation")


class AmortissementCreate(AmortissementBase):
    """Schéma pour créer un amortissement"""
    pass


class AmortissementUpdate(BaseModel):
    """Schéma pour mettre à jour un amortissement"""
    exercice: Optional[int] = Field(None, ge=2000, le=2100)
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None
    dotation: Optional[Decimal] = Field(None, ge=0)
    amortissement_cumule: Optional[Decimal] = Field(None, ge=0)
    valeur_nette_comptable: Optional[Decimal] = Field(None, ge=0)


class AmortissementInDB(AmortissementBase):
    """Schéma pour un amortissement en base de données"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class AmortissementResponse(AmortissementInDB):
    """Schéma de réponse pour un amortissement"""
    pass
