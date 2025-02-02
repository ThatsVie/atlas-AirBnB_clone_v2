#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000.
Defines a Flask application with six routes:
- "/" displays "Hello HBNB!"
- "/hbnb" displays "HBNB"
- "/c/<text>" displays "C " followed by the value of the
text variable, replacing underscores with spaces.
- "/python/<text>" displays "Python ",
followed by the value of the text variable
- "/number/<n>" displays "<n> is a number" only if n is an integer
- "/number_template/<n>" displays an HTML page only if n is an integer.
The page contains an H1 tag with "Number: n" inside the body tag.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when accessing root route ("/").
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing the "/hbnb" route.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays "C " followed by the value of the text variable,
    replacing underscores with spaces.

    Args:
    - text: text variable from the URL path.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Displays "Python ", followed by the value of the text variable,
    replacing underscores with spaces.

    Args:
    - text: text variable from the URL path.
    - default value of text is "is cool"
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays "<n> is a number" only if n is an integer.

    Args:
    - n: integer variable from the URL path.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with "Number: n" inside an H1 tag in the body,
    only if n is an integer.

    Args:
    - n: integer variable from the URL path.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
