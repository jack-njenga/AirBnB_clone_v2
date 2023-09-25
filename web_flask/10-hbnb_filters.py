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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page like 6-index.html
    """
    states = list(storage.all("State").values())
    sorted_states = sorted(states, key=lambda st: st.name)
    amenities = list(storage.all("Amenity").values())
    sorted_amenities = sorted(amenities, key=lambda amt: amt.name)
    return render_template("10-hbnb_filters.html",
                           states=sorted_states, amenities=sorted_amenities)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
