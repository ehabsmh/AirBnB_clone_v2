#!/usr/bin/python3
"""This module creates route for /states_list"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """Removes the current session for each HTTP request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display hbnb"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    states = {value.name: value.cities for value in states.values()}
    amenities = [value.name for value in amenities.values()]
    return render_template("10-hbnb_filters.html", states=states,
                           amenitiess=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
