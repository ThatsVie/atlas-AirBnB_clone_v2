#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000.
Defines Flask application with two routes
"/" displays "Hello HBNB!"
"/hbnb" displays "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Generates "Hello HBNB!", to be displayed when accessing root route ("/").
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing the "/hbnb" route.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
