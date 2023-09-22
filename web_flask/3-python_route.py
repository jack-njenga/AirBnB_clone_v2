#!/usr/bin/python3
"""
Starts a Flask web application:
    listens on 0.0.0.0, port 5000
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


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_display(text="is cool"):
    """
    Display “Python ”, followed by the value of the text variable.
    """
    if text:
        text = text.replace("_", " ")
        return f"Python {text}"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
