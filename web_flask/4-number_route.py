#!/usr/bin/python3
"""[script that starts a Flask web application]
"""
from flask import Flask

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
    if isinstance(n, int):
        return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
