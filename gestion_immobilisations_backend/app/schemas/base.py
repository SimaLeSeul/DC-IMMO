from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class TimestampSchema(BaseModel):
    """Schéma de base avec timestamps"""
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BaseResponse(BaseModel):
    """Schéma de base pour les réponses"""
    model_config = ConfigDict(from_attributes=True)


class PaginationParams(BaseModel):
    """Paramètres de pagination"""
    skip: int = 0
    limit: int = 100


class PaginatedResponse(BaseModel):
    """Réponse paginée"""
    total: int
    skip: int
    limit: int
    items: list

    model_config = ConfigDict(from_attributes=True)
