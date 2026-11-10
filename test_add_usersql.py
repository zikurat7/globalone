import os
import uuid
import psycopg

from add_usersql import add_user


def test_add_user():
    # Generate a unique email
    email = f"pytest_{uuid.uuid4().hex}@example.com"

    try:
        # Insert a test user
        user_id = add_user("Test User", 28, email)

        # Check that an ID was returned
        assert user_id is not None

        # Retrieve the inserted user
        with psycopg.connect(
            host="localhost",
            port=5432,
            dbname="globalone",
            user="postgres",
            password=os.getenv("PGPASSWORD"),
        ) as connection:

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name, age, email FROM users WHERE id = %s",
                    (user_id,),
                )

                user = cursor.fetchone()

        # Verify the database record
        assert user == ("Test User", 28, email)

    finally:
        # Delete the test record
        with psycopg.connect(
            host="localhost",
            port=5432,
            dbname="globalone",
            user="postgres",
            password=os.getenv("PGPASSWORD"),
        ) as connection:

            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM users WHERE email = %s",
                    (email,),
                )
