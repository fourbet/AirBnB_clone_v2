#!/usr/bin/python3
"""Web framework"""
from flask import Flask
from flask import render_template


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

@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ display Python , followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
    return 'Python %s' % text

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display n is a number only if n is an integer"""
    return '%d is a number' % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', nbr=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def nbr_odd_even(n):
    """  display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', nbr=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
