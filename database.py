import sqlite3


DATABASE = "app.db"


def get_user_by_name(username):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #1: String concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor = conn.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user


def get_user_by_id(user_id):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()
    return user


def authenticate_user(username, password):
    conn = sqlite3.connect(DATABASE)

    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor = conn.execute(query, (username, password))
    user = cursor.fetchone()

    conn.close()
    return user


def search_products(search_term, category):
    conn = sqlite3.connect(DATABASE)

    query = "SELECT * FROM products WHERE name LIKE ? AND category = ?"

    cursor = conn.execute(query, (f"%{search_term}%", category))
    products = cursor.fetchall()

    conn.close()
    return products


def get_products_sorted(sort_column):
    conn = sqlite3.connect(DATABASE)

    allowed_columns = {"id", "name", "category", "price"}
    if sort_column not in allowed_columns:
        sort_column = "id"
    query = f"SELECT * FROM products ORDER BY {sort_column}"

    cursor = conn.execute(query)
    products = cursor.fetchall()

    conn.close()
    return products


def safe_get_user(username):
    conn = sqlite3.connect(DATABASE)

    # SAFE: Parameterized query
    query = "SELECT * FROM users WHERE username = ?"

    cursor = conn.execute(query, (username,))
    user = cursor.fetchone()

    conn.close()
    return user