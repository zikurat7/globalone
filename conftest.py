import os
import pytest
import psycopg
from sqlalchemy import create_engine
from globalone.models import Base


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    database_url = f"postgresql://postgres:{os.getenv('PGPASSWORD')}@localhost:5432/globalone"
    engine = create_engine(database_url)

    Base.metadata.create_all(engine)

    yield

    Base.metadata.drop_all(engine)
    engine.dispose()
