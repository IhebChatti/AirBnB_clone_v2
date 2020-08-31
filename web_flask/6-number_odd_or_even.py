#!/usr/bin/python3
"""[script that starts a Flask web application]
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """[helloHBNB method]

    Returns:
        [str]: [returns Hello HBNB!]
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """[HBNB method]

    Returns:
        [str]: [returns HBNB]
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """[C <text> method]

    Args:
        text ([str]): [the text to be returned after C]

    Returns:
        [str]: [text to be returned]
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def pythonIsCool(text):
    """[python routing methid]

    Args:
        text (str, optional): [text to be put in url]. Defaults to 'is cool'.

    Returns:
        [str]: [text to be returned]
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """[number route]

    Args:
        n ([int]): [number passed]

    Returns:
        [str]: [text to be returned wheather int or 404]
    """
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """[numberTemplate]

    Args:
        n ([int]): [number passed]

    Returns:
        [html]: [fetches html page]
    """
    if isinstance(n, int):
        return render_template('5-number.html')


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddEven(n):
    """[odd or even]

    Args:
        n ([int]): [number passed]

    Returns:
        [html]: [fetches html page]
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
