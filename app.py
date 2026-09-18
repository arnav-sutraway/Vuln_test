from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/user")
def user():

    username = request.args.get("username")

    connection = sqlite3.connect("users.db")

    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)

    return str(cursor.fetchall())