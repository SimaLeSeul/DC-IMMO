from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
from app.schemas.base import TimestampSchema


# ===== USER =====

class UserBase(BaseModel):
    """Schéma de base pour User"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    language: str = Field(default='fr', pattern='^(fr|en)$')
    is_active: bool = True


class UserCreate(UserBase):
    """Schéma pour la création d'un User"""
    password: str = Field(..., min_length=8, max_length=100)
    is_superuser: bool = False
    role_ids: List[int] = []
    societe_ids: List[int] = []
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Le mot de passe doit contenir au moins 8 caractères')
        if not any(char.isdigit() for char in v):
            raise ValueError('Le mot de passe doit contenir au moins un chiffre')
        if not any(char.isupper() for char in v):
            raise ValueError('Le mot de passe doit contenir au moins une majuscule')
        return v


class UserUpdate(BaseModel):
    """Schéma pour la mise à jour d'un User"""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=100)
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    language: Optional[str] = Field(None, pattern='^(fr|en)$')
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    role_ids: Optional[List[int]] = None
    societe_ids: Optional[List[int]] = None


class UserInDB(UserBase, TimestampSchema):
    """Schéma User en base de données"""
    id: int
    is_superuser: bool
    is_deleted: int
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class User(UserInDB):
    """Schéma User complet pour les réponses API"""
    pass


class UserWithRoles(User):
    """Schéma User avec ses rôles"""
    roles: List['RoleSimple'] = []
    societes: List['SocieteSimple'] = []


# Schémas simplifiés pour éviter les références circulaires
class UserSimple(BaseModel):
    """Schéma User simplifié"""
    id: int
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# ===== AUTHENTICATION =====

class Token(BaseModel):
    """Schéma pour le token JWT"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Schéma pour le payload du token"""
    sub: Optional[int] = None
    exp: Optional[int] = None


class LoginRequest(BaseModel):
    """Schéma pour la requête de connexion"""
    username: str
    password: str


class PasswordChange(BaseModel):
    """Schéma pour le changement de mot de passe"""
    old_password: str
    new_password: str = Field(..., min_length=8, max_length=100)
    
    @field_validator('new_password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Le mot de passe doit contenir au moins 8 caractères')
        if not any(char.isdigit() for char in v):
            raise ValueError('Le mot de passe doit contenir au moins un chiffre')
        if not any(char.isupper() for char in v):
            raise ValueError('Le mot de passe doit contenir au moins une majuscule')
        return v


class PasswordReset(BaseModel):
    """Schéma pour la réinitialisation de mot de passe"""
    email: EmailStr


# Import pour les types forward ref
from app.schemas.role import RoleSimple  # noqa
from app.schemas.societe import SocieteSimple  # noqa

UserWithRoles.model_rebuild()
