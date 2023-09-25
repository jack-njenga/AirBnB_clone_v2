#!/usr/bin/python3
"""
Starts a Flask web application:
    listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ says hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ same """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ Display “C ”, followed by the value of the text variable. """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={"text": "id cool"}, strict_slashes=False)
@app.route("/python/<text>")
def py_disp(text):
    """ Display “Python ”, followed by the value of the text variable """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number(n):
    """ Display “n is a number” only if n is an integer """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def template(n):
    """ Display a HTML page only if n is an integer. """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_num(n):
    """ Display a HTML page only if n is an integer. """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
