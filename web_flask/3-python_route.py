#!/usr/bin/python3
"""Web framework"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C  followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ display Python , followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
    return 'Python %s' % text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
