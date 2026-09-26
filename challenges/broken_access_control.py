from flask import Flask, jsonify


app = Flask(__name__)

DEMO_USERS = {
    1: {"username": "alice", "email": "alice@example.test", "role": "user"},
    2: {"username": "bob", "email": "bob@example.test", "role": "admin"},
}


@app.route("/profile/<int:user_id>")
def profile(user_id):
    # Intentionally missing authentication and ownership checks (IDOR).
    user = DEMO_USERS.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)