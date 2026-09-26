from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

DATABASE = "app.db"


# Hardcoded Secret #4
ADMIN_API_TOKEN = "ARGUS_FAKE_ADMIN_TOKEN_987654321"


def save_comment(username, comment):
    conn = sqlite3.connect(DATABASE)

    query = "INSERT INTO comments (username, comment) VALUES (?, ?)"

    conn.execute(query, (username, comment))
    conn.commit()
    conn.close()


@app.route("/admin/comments")
def admin_comments():
    conn = sqlite3.connect(DATABASE)

    comments = conn.execute(
        "SELECT username, comment FROM comments"
    ).fetchall()

    conn.close()

    # Stored XSS #3: Comments rendered without escaping
    return render_template(
        "admin.html",
        comments=comments
    )


@app.route("/admin/search")
def admin_search():
    search_term = request.args.get("q", "")

    conn = sqlite3.connect(DATABASE)

    # SQL Injection demonstration retained for the training app.
    query = f"SELECT * FROM audit_logs WHERE action LIKE '%{search_term}%'"

    results = conn.execute(query).fetchall()

    conn.close()

    return {"results": results}