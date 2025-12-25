# backend/alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
from pathlib import Path

# Ajouter le dossier parent au path pour importer nos modules
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.core.config import settings
from app.core.database import Base
from app.models import User, Societe, Immobilisation  # Import tous les modèles

# Configuration Alembic
config = context.config

# Utiliser notre URL de BDD depuis settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Configuration du logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Métadonnées des modèles SQLAlchemy
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Migrations en mode 'offline' (génération de SQL sans connexion)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Migrations en mode 'online' (avec connexion active)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Détection du mode (offline vs online)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
