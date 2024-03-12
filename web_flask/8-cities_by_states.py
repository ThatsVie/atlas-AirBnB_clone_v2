#!/usr/bin/python3
"""
Starts a Flask web application listening on port 5000.
- /cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage
sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B> +
UL tag: with the list of City objects linked to the State sorted by name
LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a list of states and their associated cities
    """
    states_dict = storage.all(State)
    states = {state_id: state for state_id, state in states_dict.items()}
    # Sort states by name
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    # Sort cities within each state by name
    for state in sorted_states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
