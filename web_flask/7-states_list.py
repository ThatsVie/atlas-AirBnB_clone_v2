#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000.
Defines a Flask application with eight routes:
- "/" displays "Hello HBNB!"
- "/hbnb" displays "HBNB"
- "/c/<text>" displays "C " followed by the value of the
text variable, replacing underscores with spaces.
- "/python/<text>" displays "Python ",
followed by the value of the text variable
- "/number/<n>" displays "<n> is a number" only if n is an integer
- "/number_template/<n>" displays an HTML page only if n is an integer.
The page contains an H1 tag with "Number: n" inside the body tag.
- /number_odd_or_even/<n>: display a HTML page only if n is an integer
The page contains an H1 tag with Number: n is even|odd if n is an integer
- /states_list displays a list of all State objects sorted by name
H1 tag: "States"
UL tag: with the list of all State objects present in DBStorage
sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask
from flask import render_template
from models import storage

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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page with 'Number: n is even|odd' inside an H1 tag
    in the body,only if n is an integer.

    Args:
    - n: integer variable from the URL path.
    """
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Displays a list of states.
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
