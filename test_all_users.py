import os
import uuid
import psycopg

from dotenv import load_dotenv
from add_usersql import add_user
from all_users import get_all_users

load_dotenv()


def test_get_all_users():
    email = f"pytest_{uuid.uuid4().hex}@example.com"

    try:
        # Create a test user
        user_id = add_user("Test User", 28, email)

        # Retrieve all users
        users = get_all_users()

        # Find our test user
        test_user = next(user for user in users if user[0] == user_id)

        # Verify the data
        assert test_user[1] == "Test User"
        assert test_user[2] == 28
        assert test_user[3] == email

    finally:
        # Clean up the test user
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
