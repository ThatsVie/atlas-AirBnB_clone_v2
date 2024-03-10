#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000.
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
