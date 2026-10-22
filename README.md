# CodeNest Academy

A training academy website built with Flask and MySQL. Students can register for a course, and their details and resume are saved.

## Features
- Home page and registration page
- Registration form saved to a MySQL database
- Resume upload (PDF or Word, max 2 MB)
- Database password kept safe in a `.env` file

## Tech Stack
Python, Flask, MySQL, HTML, CSS

## Setup
1. Clone the project and open the folder
2. Create a virtual environment and install the libraries:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
3. Create a `.env` file in the project folder:
```
DB_PASSWORD=your_mysql_password
```
4. Create the database and table (run once):
```
python setup_db.py
python add_column.py
```
5. Start the app:
```
python app.py
```
6. Open `http://127.0.0.1:5000`

## Pages
| URL | Description |
|-----|-------------|
| / | Home page |
| /register | Registration form |

## Project Structure
```
academy-app/
├── app.py
├── setup_db.py
├── add_column.py
├── view_data.py
├── templates/
└── static/
```