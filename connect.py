import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="globalone",
    user="postgres",
    password="25426",
)

cursor = connection.cursor()

# Retrieve all users
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
connection.close()
