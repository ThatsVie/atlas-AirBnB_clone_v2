#!/usr/bin/python3
"""
Starts a Flask web application
Listens to host='0.0.0.0', port=5000
- /hbnb_filters: display a HTML page
"""
import sys
import os

from flask import Flask
from flask import render_template
from models import storage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
