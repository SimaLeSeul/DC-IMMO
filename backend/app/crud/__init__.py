# backend/app/crud/__init__.py
from app.crud.user import user
from app.crud.societe import societe
from app.crud.immobilisation import immobilisation

__all__ = ["user", "societe", "immobilisation"]
