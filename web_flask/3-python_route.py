#!/usr/bin/python3
"""This module starts a Flask web application on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays “C ” followed by the value of the text variable
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_python(text="is cool"):
    """Displays “Python ” followed by the value of the text variable
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
