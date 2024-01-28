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


@app.route("/states_list", strict_slashes=False)
def get_states():
    """Displays all states in a HTML file"""    
    states = storage.all(State)
    states = {value.id: value.name for value in states.values()}
    return render_template("7-states_list.html", 
                           tablename="States",
                           states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
