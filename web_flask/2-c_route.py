#!/usr/bin/python3
"""
Starts a Flask web application:
    listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    Displays “C ” followed by the value of the text variable.
    """
    if text:
        text = text.replace("_", " ")
        return f"C {text}"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
