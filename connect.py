import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("PGPASSWORD")

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="globalone",
    user="postgres",
    password=password,
)

cursor = connection.cursor()

# Retrieve all users
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
connection.close()
