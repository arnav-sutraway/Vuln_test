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

    # SQL Injection #2: User-controlled ID
    query = f"SELECT * FROM users WHERE id = {user_id}"

    cursor = conn.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user


def authenticate_user(username, password):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #3: Login query using interpolation
    query = (
        f"SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    cursor = conn.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user


def search_products(search_term, category):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #4: Multiple user inputs in dynamic query
    query = (
        "SELECT * FROM products "
        "WHERE name LIKE '%"
        + search_term
        + "%' AND category = '"
        + category
        + "'"
    )

    cursor = conn.execute(query)
    products = cursor.fetchall()

    conn.close()
    return products


def get_products_sorted(sort_column):
    conn = sqlite3.connect(DATABASE)

    # SQL Injection #5: Unsanitized ORDER BY column
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