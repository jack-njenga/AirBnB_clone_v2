#!/usr/bin/python3
"""
Starts a Flask web application:
    listens on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ says hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ same """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text():
    """ text """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_dist(text):
    """ text """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ numbers """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_int(n):
    """ Display a HTML page only if n is an integer: """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
