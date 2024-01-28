#!/usr/bin/python3
"""This module creates route for /states_list"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """Removes the current session for each HTTP request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def get_cities_by_states():
    """Displays all cities by state in a HTML file"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html",
                           tablename="States",
                           states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
