# backend/app/models/__init__.py
from app.models.user import User
from app.models.societe import Societe
from app.models.categorie import Categorie
from app.models.immobilisation import Immobilisation
from app.models.amortissement import Amortissement  # ← AJOUTÉ
from app.db.base_class import Base

__all__ = ["User", "Societe", "Categorie", "Immobilisation", "Amortissement"]  # ← AJOUTÉ
