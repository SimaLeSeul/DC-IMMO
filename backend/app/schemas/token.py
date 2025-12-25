# app/schemas/token.py
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Schéma pour le token JWT."""
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Schéma pour le payload du token."""
    sub: Optional[int] = None  # user_id
    exp: Optional[int] = None  # expiration timestamp
