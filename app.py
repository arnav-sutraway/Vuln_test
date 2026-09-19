from flask import Flask, request, render_template, Response
from markupsafe import Markup
from database import get_user_by_name, get_user_by_id


app = Flask(__name__)


@app.route("/search")
def search():
    query = request.args.get("q", "")

    # XSS #1: Reflected XSS through raw HTML response
    html = f"""
    <html>
        <body>
            <h1>Search Results</h1>
            <p>You searched for: {query}</p>
        </body>
    </html>
    """

    return Response(html, content_type="text/html")


@app.route("/profile")
def profile():
    username = request.args.get("username", "Guest")

    # XSS #2: Explicitly marking user input as safe HTML
    unsafe_content = Markup(
        f"<div class='profile'>Welcome, {username}</div>"
    )

    return unsafe_content


@app.route("/user")
def user_lookup():
    username = request.args.get("username", "")

    # SQL Injection #8: Vulnerability through imported database function
    user = get_user_by_name(username)

    return {
        "username": username,
        "user": str(user)
    }


@app.route("/user-by-id")
def user_by_id():
    user_id = request.args.get("id", "")

    # SQL Injection #9: User-controlled ID passed to vulnerable function
    user = get_user_by_id(user_id)

    return {
        "user": str(user)
    }


@app.route("/safe-search")
def safe_search():
    query = request.args.get("q", "")

    # SAFE: Jinja2 escapes the variable by default
    return render_template("search.html", query=query)


if __name__ == "__main__":
    app.run(debug=True)