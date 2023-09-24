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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display a HTML page like 8-index.html
    """
    states = list(storage.all("State").values())
    sorted_states = sorted(states, key=lambda st: st.name)

    amenities = list(storage.all("Amenity").values())
    sorted_amenities = sorted(amenities, key=lambda amt: amt.name)

    places = list(storage.all("Place").values())
    sorted_places = sorted(places, key=lambda plc: plc.name)
    return render_template("100-hbnb.html", states=sorted_states,
                           amenities=sorted_amenities, places=sorted_places)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
