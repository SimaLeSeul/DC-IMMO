from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.base import TimestampSchema


class RoleBase(BaseModel):
    """Schéma de base pour Role"""
    name: str = Field(..., min_length=1, max_length=100)
    code: str = Field(..., min_length=1, max_length=50, pattern='^[A-Z_]+$')
    description: Optional[str] = None
    permissions: Dict[str, Any] = Field(default_factory=dict)


class RoleCreate(RoleBase):
    """Schéma pour la création d'un Role"""
    pass


class RoleUpdate(BaseModel):
    """Schéma pour la mise à jour d'un Role"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    permissions: Optional[Dict[str, Any]] = None


class RoleInDB(RoleBase, TimestampSchema):
    """Schéma Role en base de données"""
    id: int

    model_config = ConfigDict(from_attributes=True)


class Role(RoleInDB):
    """Schéma Role complet pour les réponses API"""
    pass


class RoleSimple(BaseModel):
    """Schéma Role simplifié"""
    id: int
    name: str
    code: str

    model_config = ConfigDict(from_attributes=True)
