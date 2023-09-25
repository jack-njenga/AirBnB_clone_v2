#!/usr/bin/python3
"""
Starts a Flask web application:
    listinging on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    says hello
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    same
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    Displays “C ”, followed by the value of the text variable.
    """
    if text:
        return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def py_diplay(text):
    """
    Displays “Python ”, followed by the value of the text variable.
    """
    if text:
        text = text.replace("_", " ")
        return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def n_display(n):
    """
    Displays “n is a number” only if n is an Integer
    """
    if n:
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
