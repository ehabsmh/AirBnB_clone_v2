#!/usr/bin/python3
"""This module starts a Flask web application on 0.0.0.0, port 5000"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>")
def display_n(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def display_html_n(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def display_html_odd_even_n(n):
    """display a HTML page only if n is an integer"""
    result = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', num=n, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
