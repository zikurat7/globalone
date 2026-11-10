import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def add_user(name, age, email):
    password = os.getenv("PGPASSWORD")

    if not password:
        raise RuntimeError("Please set the PGPASSWORD environment variable.")

    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="globalone",
        user="postgres",
        password=password,
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (name, age, email)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (name, age, email),
            )

            user_id = cursor.fetchone()[0]

    return user_id


def main():
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    email = input("Enter email: ").strip()

    user_id = add_user(name, age, email)

    print(f"User successfully added! ID: {user_id}")


if __name__ == "__main__":
    main()
