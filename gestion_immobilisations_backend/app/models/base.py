from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declared_attr


class TimestampMixin:
    """Mixin pour ajouter les timestamps de création et modification"""
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class SoftDeleteMixin:
    """Mixin pour la suppression logique"""
    
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Integer, default=0, nullable=False)  # 0=actif, 1=supprimé
