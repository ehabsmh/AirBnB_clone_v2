#!/usr/bin/python3
"""This module starts a Flask web application on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


app.run(host='0.0.0.0', port=5000)