# backend/app/schemas/immobilisation.py
from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


# Propriétés partagées
class ImmobilisationBase(BaseModel):
    code: str = Field(..., min_length=1, max_length=50, description="Code unique de l'immobilisation")
    libelle: str = Field(..., min_length=1, max_length=200, description="Libellé de l'immobilisation")
    societe_id: int = Field(..., gt=0, description="ID de la société propriétaire")
    categorie_id: Optional[int] = Field(None, gt=0, description="ID de la catégorie")
    
    valeur_acquisition: Decimal = Field(..., gt=0, description="Valeur d'acquisition HT")
    valeur_residuelle: Optional[Decimal] = Field(None, ge=0, description="Valeur résiduelle estimée")
    
    date_acquisition: date = Field(..., description="Date d'acquisition")
    date_mise_en_service: Optional[date] = Field(None, description="Date de mise en service")
    
    duree_amortissement: int = Field(..., gt=0, le=100, description="Durée d'amortissement en années")
    is_active: bool = Field(default=True, description="Immobilisation active")


# Propriétés pour la création
class ImmobilisationCreate(ImmobilisationBase):
    """Schéma pour créer une immobilisation."""
    pass


# Propriétés pour la mise à jour (tous les champs optionnels)
class ImmobilisationUpdate(BaseModel):
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    libelle: Optional[str] = Field(None, min_length=1, max_length=200)
    categorie_id: Optional[int] = Field(None, gt=0)
    
    valeur_acquisition: Optional[Decimal] = Field(None, gt=0)
    valeur_residuelle: Optional[Decimal] = Field(None, ge=0)
    
    date_acquisition: Optional[date] = None
    date_mise_en_service: Optional[date] = None
    
    duree_amortissement: Optional[int] = Field(None, gt=0, le=100)
    is_active: Optional[bool] = None


# Propriétés en base de données (lecture seule)
class ImmobilisationInDBBase(ImmobilisationBase):
    id: int
    created_at: date
    updated_at: Optional[date] = None
    
    model_config = ConfigDict(from_attributes=True)


# Schéma pour les réponses API
class Immobilisation(ImmobilisationInDBBase):
    """Schéma complet pour les réponses."""
    pass


# Schéma avec relations (pour les réponses détaillées)
class ImmobilisationWithRelations(Immobilisation):
    """Schéma avec relations chargées."""
    societe: Optional[dict] = None
    categorie: Optional[dict] = None
    amortissements: list = []
