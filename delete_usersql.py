import os

import psycopg
from dotenv import load_dotenv

from all_users import get_all_users

load_dotenv()


def delete_user(user_id):
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
            cursor.execute(
                "DELETE FROM users WHERE id = %s RETURNING id;",
                (user_id,),
            )
            deleted_user = cursor.fetchone()

    return deleted_user is not None


def main():
    users = get_all_users()

    if not users:
        print("There are no users to delete.")
        return

    print("Users:")
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]} | Age: {user[2]} | Email: {user[3]}")

    user_id = int(input("Enter the ID of the user to delete: ").strip())

    if delete_user(user_id):
        print(f"User with ID {user_id} successfully deleted.")
    else:
        print(f"No user found with ID {user_id}.")


if __name__ == "__main__":
    main()
