# backend/app/schemas/societe.py
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

# Schéma de base
class SocieteBase(BaseModel):
    code: str = Field(..., min_length=1, max_length=20, description="Code unique de la société")
    raison_sociale: str = Field(..., min_length=1, max_length=255)
    siret: Optional[str] = Field(None, min_length=14, max_length=14, pattern=r'^\d{14}$')
    adresse: Optional[str] = None
    code_postal: Optional[str] = Field(None, max_length=10)
    ville: Optional[str] = Field(None, max_length=100)
    pays: str = Field(default="FRA", max_length=3, description="Code ISO 3166-1 alpha-3")
    telephone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None

# Schéma pour la création
class SocieteCreate(SocieteBase):
    pass

# Schéma pour la mise à jour
class SocieteUpdate(BaseModel):
    code: Optional[str] = Field(None, min_length=1, max_length=20)
    raison_sociale: Optional[str] = Field(None, min_length=1, max_length=255)
    siret: Optional[str] = Field(None, min_length=14, max_length=14, pattern=r'^\d{14}$')
    adresse: Optional[str] = None
    code_postal: Optional[str] = Field(None, max_length=10)
    ville: Optional[str] = Field(None, max_length=100)
    pays: Optional[str] = Field(None, max_length=3)
    telephone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

# Schéma de retour
class Societe(SocieteBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Schéma pour la liste
class SocieteInList(BaseModel):
    id: int
    code: str
    raison_sociale: str
    ville: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True
