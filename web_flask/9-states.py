#!/usr/bin/python3
"""Web framework"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """display a HTML"""
    states = storage.all(State)
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None

    else:
        states = states.values()
    return render_template('9-states.html', st_storage=states, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
