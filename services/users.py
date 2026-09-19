import sqlite3


def find_users(email, role):
    conn = sqlite3.connect("app.db")

    # SQL Injection #12: Multiple concatenated inputs
    query = (
        "SELECT * FROM users "
        "WHERE email = '" + email + "' "
        "AND role = '" + role + "'"
    )

    users = conn.execute(query).fetchall()

    conn.close()
    return users


def delete_user(user_id):
    conn = sqlite3.connect("app.db")

    # SQL Injection #13
    query = f"DELETE FROM users WHERE id = {user_id}"

    conn.execute(query)
    conn.commit()
    conn.close()