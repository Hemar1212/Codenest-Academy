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

try:
    cursor.execute("ALTER TABLE registrations ADD COLUMN resume_filename VARCHAR(255)")
    conn.commit()
    print("Column added!")
except mysql.connector.Error as e:
    print("Skipped:", e)

cursor.close()
conn.close()