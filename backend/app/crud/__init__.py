"""
Export des opérations CRUD
"""

from app.crud import crud_categorie
from app.crud.crud_societe import crud_societe
from app.crud import crud_user
from app.crud import crud_immobilisation

__all__ = [
    "crud_categorie",
    "crud_societe",
    "crud_user",
    "crud_immobilisation",
]
