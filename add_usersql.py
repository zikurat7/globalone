import os
import psycopg

# Get database password from environment
password = os.getenv("PGPASSWORD")

if not password:
    raise SystemExit("Please set the PGPASSWORD environment variable.")

# Ask user for information
name = input("Enter name: ").strip()
age = int(input("Enter age: "))
email = input("Enter email: ").strip()

# Connect to PostgreSQL
with psycopg.connect(
    host="localhost", port=5432, dbname="globalone", user="postgres", password=25426
) as connection:

    with connection.cursor() as cursor:

        # Insert user into database
        cursor.execute(
            """
            INSERT INTO users (name, age, email)
            VALUES (%s, %s, %s)
            RETURNING id;
            """,
            (name, age, email),
        )

        user_id = cursor.fetchone()[0]

print(f"User successfully added! ID: {user_id}")
