#!/usr/bin/python3
"""
Starts a Flask web application:
    listens on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    Removes the current SQLAlchemy Session:
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_states():
    """
    Display the "States" HTML page
    """
    states = list(storage.all("State").values())
    sorted_states = sorted(states, key=lambda st: st.name)
    return render_template("7-states_list.html", states=sorted_states)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
