import sqlite3


def find_users(email, role):
    conn = sqlite3.connect("app.db")

    query = (
        "SELECT * FROM users "
        "WHERE email = ? AND role = ?"
    )

    users = conn.execute(query, (email, role)).fetchall()

    conn.close()
    return users


def delete_user(user_id):
    conn = sqlite3.connect("app.db")

    query = "DELETE FROM users WHERE id = ?"

    conn.execute(query, (user_id,))
    conn.commit()
    conn.close()