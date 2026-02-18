from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
from app.core.config import get_settings
from app.models import Base  # This imports all models via __init__.py

# 1. Load context config and settings
config = context.config
settings = get_settings()

# 2. Inject our DATABASE_URL from .env into Alembic
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# 3. Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. Point Alembic to our models
target_metadata = Base.metadata

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()