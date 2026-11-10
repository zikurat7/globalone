# This is a testing project for a sole purpose of learning python
maybe one day i will become a full-stack python developer =)

## First SQLAlchemy model

`src/globalone/models.py` defines a `User` model mapped to the existing
`users` table. `Base` is the shared declarative base; SQLAlchemy registers
each model's table in `Base.metadata`, which Alembic uses to compare models
with the database.

The model describes the table; it does not create or modify the database by
itself. Use an Alembic migration when you need to change the database schema.

To run the ORM example with PostgreSQL in Docker, run:

```bash
docker compose run --build --rm app
```

Compose starts the database if needed. The app applies pending migrations and
then runs `orm_example.py` inside the container, where it connects to `db:5432`.