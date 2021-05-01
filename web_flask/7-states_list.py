#!/usr/bin/python3
"""Web framework"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML"""
    dict = storage.all(State)
    return render_template('7-states_list.html', storage=dict)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
