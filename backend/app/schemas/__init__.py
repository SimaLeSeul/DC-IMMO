"""
Schémas Pydantic
"""

from .user import User, UserCreate, UserUpdate, UserInDB
from .societe import SocieteBase, SocieteCreate, SocieteUpdate, SocieteInDB, SocieteResponse
from .categorie import CategorieBase, CategorieCreate, CategorieUpdate, CategorieInDB, CategorieResponse
from .immobilisation import (
    ImmobilisationBase,
    ImmobilisationCreate,
    ImmobilisationUpdate,
    ImmobilisationInDB,
    ImmobilisationResponse,
    ImmobilisationWithDetails
)
from .amortissement import (
    AmortissementBase,
    AmortissementCreate,
    AmortissementUpdate,
    AmortissementInDB,
    AmortissementResponse
)

__all__ = [
    # User
    "User",
    "UserCreate",
    "UserUpdate",
    "UserInDB",
    # Societe
    "SocieteBase",
    "SocieteCreate",
    "SocieteUpdate",
    "SocieteInDB",
    "SocieteResponse",
    # Categorie
    "CategorieBase",
    "CategorieCreate",
    "CategorieUpdate",
    "CategorieInDB",
    "CategorieResponse",
    # Immobilisation
    "ImmobilisationBase",
    "ImmobilisationCreate",
    "ImmobilisationUpdate",
    "ImmobilisationInDB",
    "ImmobilisationResponse",
    "ImmobilisationWithDetails",
    # Amortissement
    "AmortissementBase",
    "AmortissementCreate",
    "AmortissementUpdate",
    "AmortissementInDB",
    "AmortissementResponse",
]
