"""
Schémas Pydantic pour les utilisateurs
"""

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Schéma de base pour un utilisateur"""
    email: EmailStr = Field(..., description="Email de l'utilisateur")
    username: str = Field(..., min_length=3, max_length=50, description="Nom d'utilisateur")
    nom: Optional[str] = Field(None, max_length=100, description="Nom")
    prenom: Optional[str] = Field(None, max_length=100, description="Prénom")
    is_active: bool = Field(default=True, description="Utilisateur actif")
    is_superuser: bool = Field(default=False, description="Super utilisateur")


class UserCreate(UserBase):
    """Schéma pour créer un utilisateur"""
    password: str = Field(..., min_length=8, description="Mot de passe")


class UserUpdate(BaseModel):
    """Schéma pour mettre à jour un utilisateur"""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    nom: Optional[str] = Field(None, max_length=100)
    prenom: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=8)
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserInDB(UserBase):
    """Schéma pour un utilisateur en base de données"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class User(UserInDB):
    """Schéma de réponse pour un utilisateur"""
    pass
