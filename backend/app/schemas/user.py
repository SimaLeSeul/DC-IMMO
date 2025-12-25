# backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Schéma de base pour un utilisateur."""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    nom: str = Field(..., min_length=1, max_length=100)
    prenom: str = Field(..., min_length=1, max_length=100)
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    """Schéma pour créer un utilisateur."""
    password: str = Field(..., min_length=8, max_length=72)
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Valide que le mot de passe :
        - Fait entre 8 et 72 caractères
        - Contient au moins une majuscule
        - Contient au moins un chiffre
        """
        if len(v) < 8:
            raise ValueError('Le mot de passe doit contenir au moins 8 caractères')
        if len(v) > 72:
            raise ValueError('Le mot de passe ne peut pas dépasser 72 caractères (limite bcrypt)')
        if not any(c.isupper() for c in v):
            raise ValueError('Le mot de passe doit contenir au moins une majuscule')
        if not any(c.isdigit() for c in v):
            raise ValueError('Le mot de passe doit contenir au moins un chiffre')
        return v


class UserUpdate(BaseModel):
    """Schéma pour mettre à jour un utilisateur."""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    nom: Optional[str] = Field(None, min_length=1, max_length=100)
    prenom: Optional[str] = Field(None, min_length=1, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=72)
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class User(UserBase):
    """Schéma complet avec ID et timestamps."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class UserInList(BaseModel):
    """Schéma pour afficher un utilisateur dans une liste."""
    id: int
    email: EmailStr
    username: str
    nom: str
    prenom: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
