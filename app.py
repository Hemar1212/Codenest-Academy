import os
import time
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2 MB limit
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.environ["DB_PASSWORD"],
    "database": "academy_db",
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        email = request.form["email"]
        course = request.form["course"]

        resume_filename = None
        resume = request.files.get("resume")
        if resume and resume.filename:
            if not allowed_file(resume.filename):
                return "<h2>Only PDF or Word files are allowed.</h2><a href='/register'>Go back</a>", 400
            resume_filename = f"{int(time.time())}_{secure_filename(resume.filename)}"
            resume.save(os.path.join(UPLOAD_FOLDER, resume_filename))

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registrations (name, age, gender, email, course, resume_filename) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (name, age, gender, email, course, resume_filename),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("success"))

    return render_template("register.html")


@app.route("/success")
def success():
    return "<h2>Registration successful!</h2><a href='/'>Back to home</a>"


if __name__ == "__main__":
    app.run(debug=True)