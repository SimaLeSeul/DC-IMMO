"""
Schémas Pydantic pour les immobilisations
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, TYPE_CHECKING
from datetime import date, datetime
from decimal import Decimal

if TYPE_CHECKING:
    from app.schemas.societe import SocieteResponse
    from app.schemas.categorie import CategorieResponse


class ImmobilisationBase(BaseModel):
    """Schéma de base pour une immobilisation"""
    libelle: str = Field(..., min_length=1, max_length=255, description="Libellé de l'immobilisation")
    numero_serie: Optional[str] = Field(None, max_length=100, description="Numéro de série")
    date_acquisition: date = Field(..., description="Date d'acquisition")
    valeur_acquisition: Decimal = Field(..., gt=0, description="Valeur d'acquisition HT")
    valeur_residuelle: Optional[Decimal] = Field(default=0, ge=0, description="Valeur résiduelle")
    duree_amortissement: int = Field(..., gt=0, description="Durée d'amortissement en mois")
    methode_amortissement: str = Field(default="lineaire", description="Méthode d'amortissement")
    date_mise_en_service: Optional[date] = Field(None, description="Date de mise en service")
    localisation: Optional[str] = Field(None, max_length=200, description="Localisation")
    num_facture: Optional[str] = Field(None, max_length=100, description="Numéro de facture")
    fournisseur: Optional[str] = Field(None, max_length=200, description="Fournisseur")
    
    # Clés étrangères
    societe_id: int = Field(..., description="ID de la société")
    categorie_id: int = Field(..., description="ID de la catégorie")


class ImmobilisationCreate(ImmobilisationBase):
    """Schéma pour créer une immobilisation"""
    pass


class ImmobilisationUpdate(BaseModel):
    """Schéma pour mettre à jour une immobilisation"""
    libelle: Optional[str] = Field(None, min_length=1, max_length=255)
    numero_serie: Optional[str] = Field(None, max_length=100)
    date_acquisition: Optional[date] = None
    valeur_acquisition: Optional[Decimal] = Field(None, gt=0)
    valeur_residuelle: Optional[Decimal] = Field(None, ge=0)
    duree_amortissement: Optional[int] = Field(None, gt=0)
    methode_amortissement: Optional[str] = None
    date_mise_en_service: Optional[date] = None
    localisation: Optional[str] = Field(None, max_length=200)
    num_facture: Optional[str] = Field(None, max_length=100)
    fournisseur: Optional[str] = Field(None, max_length=200)
    societe_id: Optional[int] = None
    categorie_id: Optional[int] = None


class ImmobilisationInDB(ImmobilisationBase):
    """Schéma pour une immobilisation en base de données"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    statut: str
    valeur_nette_comptable: Decimal
    created_at: datetime
    updated_at: Optional[datetime] = None


class ImmobilisationResponse(ImmobilisationInDB):
    """Schéma de réponse pour une immobilisation"""
    pass


class ImmobilisationWithDetails(ImmobilisationResponse):
    """Schéma avec détails (société, catégorie, amortissements)"""
    model_config = ConfigDict(from_attributes=True)
    
    societe: Optional["SocieteResponse"] = None
    categorie: Optional["CategorieResponse"] = None
