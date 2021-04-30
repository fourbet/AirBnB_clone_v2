#!/usr/bin/python3
"""Web framework"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display a HTML"""
    dict_st = storage.all(State).values()
    return render_template('8-cities_by_states.html', st_storage=dict_st)

@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
