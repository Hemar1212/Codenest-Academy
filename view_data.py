import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ["DB_PASSWORD"],
    database="academy_db",
)
cursor = conn.cursor()
cursor.execute("SELECT id, name, age, gender, email, course FROM registrations")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()