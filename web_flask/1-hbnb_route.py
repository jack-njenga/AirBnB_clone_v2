#!/usr/bin/python3
"""
Starts a Flask web application:
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbhb():
    """
    Return "Hello HBHB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbhb():
    """
    Returns "HBNB"
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
