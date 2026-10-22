import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(host="localhost", user="root", password=os.environ["DB_PASSWORD"])
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS academy_db")
cursor.execute("USE academy_db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(10) NOT NULL,
        email VARCHAR(120) NOT NULL,
        course VARCHAR(50) NOT NULL,
        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()
cursor.close()
conn.close()
print("Database and table are ready!")