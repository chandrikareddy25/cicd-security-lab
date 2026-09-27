import hashlib
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # B608: SQL built by string concatenation
    cur.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    return str(cur.fetchall())


def hash_password(pw):
    # B303: MD5 is cryptographically broken for password hashing
    return hashlib.md5(pw.encode()).hexdigest()


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
