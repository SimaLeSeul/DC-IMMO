from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.base import TimestampMixin
from app.models.user import user_roles  # ← IMPORT au lieu de redéfinir


class Role(Base, TimestampMixin):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    libelle = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    
    # Relations
    users = relationship("User", secondary=user_roles, back_populates="roles")
    
    def __repr__(self):
        return f"<Role(id={self.id}, code='{self.code}', libelle='{self.libelle}')>"
