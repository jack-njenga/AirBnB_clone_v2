#!/usr/bin/python3
"""
Starts a Flask web application:
    listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    closes the current sql session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def get_cities():
    """
    Displays the cities html page
    """
    states = list(storage.all("State").values())
    sorted_states = sorted(states, key=lambda st: st.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
