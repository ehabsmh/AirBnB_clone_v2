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


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def get_cities_by_states(id=None):
    """Displays all cities by state in a HTML file"""
    states = storage.all(State)

    if id:
        state_cities = []
        state_name = ""
        for state in states.values():
            if state.id == id:
                state_name = state.name
                state_cities = state.cities
        return render_template("9-states.html",
                               tablename="States",
                               state_cities=state_cities,
                               states=states,
                               id=id,
                               state_name=state_name)
    else:
        states = {value.id: value.name for value in states.values()}
        return render_template("9-states.html",
                               tablename="States",
                               states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
