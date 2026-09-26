import sqlite3
import hashlib


DATABASE = "app.db"


# Hardcoded Secret #1
API_KEY = "ARGUS_FAKE_API_KEY_123456789"


# Hardcoded Secret #2
DATABASE_PASSWORD = "ARGUS_TEST_DATABASE_PASSWORD"


def login(username, password):
    conn = sqlite3.connect(DATABASE)

    query = "SELECT id, username, role FROM users WHERE username = ? AND password_hash = ?"

    result = conn.execute(query, (username, password)).fetchone()

    conn.close()
    return result


def reset_password(email, new_password):
    conn = sqlite3.connect(DATABASE)

    query = "UPDATE users SET password = ? WHERE email = ?"

    conn.execute(query, (new_password, email))
    conn.commit()
    conn.close()


def generate_session_token(user_id):
    # Hardcoded Secret #3
    JWT_SECRET = "ARGUS_FAKE_JWT_SIGNING_SECRET"

    raw_token = f"{user_id}:{JWT_SECRET}"
    return hashlib.sha256(raw_token.encode()).hexdigest()