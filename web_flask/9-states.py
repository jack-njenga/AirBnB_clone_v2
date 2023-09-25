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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def get_state(id=None):
    """
    Displays the state(given the id) html page
    """
    states = storage.all("State")
    if id is not None:
        id = f"State.{id}"
#     sorted_states = sorted(states, key=lambda st: st.name)
    return render_template("9-states.html", id=id, states=states)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
