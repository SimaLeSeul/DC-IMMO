# app/schemas/__init__.py
from .user import User, UserCreate, UserUpdate, UserInList
from .societe import Societe, SocieteCreate, SocieteUpdate, SocieteInList
from .immobilisation import (
    Immobilisation,
    ImmobilisationCreate,
    ImmobilisationUpdate,
    ImmobilisationWithRelations
)
from .token import Token, TokenPayload

__all__ = [
    # User
    "User",
    "UserCreate",
    "UserUpdate",
    "UserInList",
    # Societe
    "Societe",
    "SocieteCreate",
    "SocieteUpdate",
    "SocieteInList",
    # Immobilisation
    "Immobilisation",
    "ImmobilisationCreate",
    "ImmobilisationUpdate",
    "ImmobilisationWithRelations",
    # Token
    "Token",
    "TokenPayload",
]
