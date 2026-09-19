import sqlite3
import hashlib


DATABASE = "app.db"


# Hardcoded Secret #1
API_KEY = "ARGUS_FAKE_API_KEY_123456789"


# Hardcoded Secret #2
DATABASE_PASSWORD = "ARGUS_TEST_DATABASE_PASSWORD"


def login(username, password):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #6
    query = (
        "SELECT id, username, role FROM users "
        f"WHERE username = '{username}' "
        f"AND password_hash = '{password}'"
    )

    result = conn.execute(query).fetchone()

    conn.close()
    return result


def reset_password(email, new_password):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #7
    query = (
        "UPDATE users SET password = '"
        + new_password
        + "' WHERE email = '"
        + email
        + "'"
    )

    conn.execute(query)
    conn.commit()
    conn.close()


def generate_session_token(user_id):
    # Hardcoded Secret #3
    JWT_SECRET = "ARGUS_FAKE_JWT_SIGNING_SECRET"

    raw_token = f"{user_id}:{JWT_SECRET}"
    return hashlib.sha256(raw_token.encode()).hexdigest()