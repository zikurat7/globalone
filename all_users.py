import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_all_users():
    password = os.getenv("PGPASSWORD")

    if not password:
        raise RuntimeError("Please set the PGPASSWORD environment variable.")

    with psycopg.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        dbname=os.getenv("PGDATABASE", "globalone"),
        user=os.getenv("PGUSER", "postgres"),
        password=password,
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()

    return users


def main():
    users = get_all_users()

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
