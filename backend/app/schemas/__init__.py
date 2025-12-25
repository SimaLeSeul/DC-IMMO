# backend/app/schemas/__init__.py
from .user import User, UserCreate, UserUpdate, UserInDB
from .societe import Societe, SocieteCreate, SocieteUpdate
from .immobilisation import (
    Immobilisation,
    ImmobilisationCreate,
    ImmobilisationUpdate,
    ImmobilisationWithRelations  # ← Changé de ImmobilisationInList
)
from .token import Token, TokenPayload

__all__ = [
    # User
    "User",
    "UserCreate",
    "UserUpdate",
    "UserInDB",
    # Societe
    "Societe",
    "SocieteCreate",
    "SocieteUpdate",
    # Immobilisation
    "Immobilisation",
    "ImmobilisationCreate",
    "ImmobilisationUpdate",
    "ImmobilisationWithRelations",  # ← Changé
    # Token
    "Token",
    "TokenPayload",
]
