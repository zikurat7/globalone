from logging.config import fileConfig
import os

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, pool

from globalone import models

load_dotenv()

password = os.getenv("PGPASSWORD")

if not password:
    raise RuntimeError("PGPASSWORD is not set")

database_url = URL.create(
    "postgresql+psycopg",
    username=os.getenv("PGUSER", "postgres"),
    password=password,
    host=os.getenv("PGHOST", "db"),
    port=int(os.getenv("PGPORT", "5432")),
    database=os.getenv("PGDATABASE", "globalone"),
)

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = models.Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

    connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
