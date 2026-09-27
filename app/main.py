import sqlite3

from flask import Flask, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return str(cur.fetchall())


def hash_password(pw):
    return generate_password_hash(pw, method="pbkdf2:sha256")


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
