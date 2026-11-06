"""SECURITY BENCHMARK FIXTURE ONLY.

Deliberately vulnerable examples for static security scanners.
No application server or fixture entrypoint is launched.
Do not copy these examples into production.
"""

import pickle
import sqlite3
import subprocess

from flask import request


def unsafe_shell_command():
    # Expected: command injection / shell=True with untrusted input.
    return subprocess.check_output(request.args["cmd"], shell=True, text=True)


def unsafe_sql_query():
    # Expected: SQL injection from URL parameter into SQL text.
    username = request.args["username"]
    database = sqlite3.connect(":memory:")
    return database.execute("SELECT * FROM accounts WHERE username = '" + username + "'").fetchone()


def unsafe_deserialization():
    # Expected: unsafe unpickling of HTTP request data.
    return pickle.loads(request.get_data())


def safe_parameterized_query(database, username):
    # Negative control: parameters instead of SQL string concatenation.
    return database.execute("SELECT * FROM accounts WHERE username = ?", (username,)).fetchone()


def safe_constant_command():
    # Negative control: no shell interpretation or user-provided arguments.
    return subprocess.run(["echo", "static-only"], shell=False, check=True)
