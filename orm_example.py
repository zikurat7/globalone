import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, select
from sqlalchemy.orm import Session

from globalone.models import User

load_dotenv()

password = os.getenv("PGPASSWORD")
if not password:
    raise RuntimeError("Please set PGPASSWORD in your environment or .env file.")

engine = create_engine(
    URL.create(
        "postgresql+psycopg",
        username=os.getenv("PGUSER", "postgres"),
        password=password,
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        database=os.getenv("PGDATABASE", "globalone"),
    )
)

with Session(engine) as session:
    user = session.scalar(select(User).where(User.email == "ava@example.com"))
    if user is None:
        user = User(name="Ava", age=28, email="ava@example.com")
        session.add(user)
        session.commit()
        print(f"Saved user with ID: {user.id}")
    else:
        print(f"User already exists with ID: {user.id}")

    print(f"{user.name}, age {user.age}, email {user.email}")
