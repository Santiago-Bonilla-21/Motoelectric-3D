import sqlite3
from pathlib import Path
import hashlib


# Ruta de la base de datos
BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "motoelectric.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS simulations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            voltage REAL,
            current REAL,
            rpm REAL,
            power REAL,
            input_teeth INTEGER,
            output_teeth INTEGER,
            efficiency REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def create_default_user():
    connection = get_connection()
    cursor = connection.cursor()

    password = hash_password("1234")

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES (?, ?)
    """, ("admin", password))

    connection.commit()
    connection.close()


def authenticate_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    hashed_password = hash_password(password)

    cursor.execute("""
        SELECT id, username
        FROM users
        WHERE username = ? AND password = ?
    """, (username, hashed_password))

    user = cursor.fetchone()

    connection.close()

    return user