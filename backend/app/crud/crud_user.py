# backend/app/crud/user.py
from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

# Contexte de hachage de mot de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """Opérations CRUD pour les utilisateurs."""

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        """Récupère un utilisateur par son email."""
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        """Récupère un utilisateur par son username."""
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """
        Crée un nouvel utilisateur avec mot de passe haché.

        Args:
            db: Session SQLAlchemy
            obj_in: Schéma UserCreate avec mot de passe en clair

        Returns:
            User créé avec mot de passe haché
        """
        db_obj = User(
            email=obj_in.email,
            username=obj_in.username,
            nom=obj_in.nom,
            prenom=obj_in.prenom,
            hashed_password=self.get_password_hash(obj_in.password),
            is_active=True,
            is_superuser=False
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, 
        db: Session, 
        *, 
        db_obj: User, 
        obj_in: UserUpdate
    ) -> User:
        """
        Met à jour un utilisateur (avec gestion du mot de passe).

        Args:
            db: Session SQLAlchemy
            db_obj: User existant
            obj_in: Schéma UserUpdate

        Returns:
            User mis à jour
        """
        update_data = obj_in.model_dump(exclude_unset=True)

        # Si un nouveau mot de passe est fourni, le hacher
        if "password" in update_data:
            hashed_password = self.get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(
        self, 
        db: Session, 
        *, 
        email: str, 
        password: str
    ) -> Optional[User]:
        """
        Authentifie un utilisateur.

        Args:
            db: Session SQLAlchemy
            email: Email de l'utilisateur
            password: Mot de passe en clair

        Returns:
            User si authentification réussie, None sinon
        """
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        """Vérifie si l'utilisateur est actif."""
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        """Vérifie si l'utilisateur est superuser."""
        return user.is_superuser

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Hache un mot de passe."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Vérifie un mot de passe contre son hash."""
        return pwd_context.verify(plain_password, hashed_password)


# Instance unique pour import
crud_user = CRUDUser(User)