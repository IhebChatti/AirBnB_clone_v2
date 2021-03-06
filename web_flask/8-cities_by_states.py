#!/usr/bin/python3
"""[summary]
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """[teardown method]
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def citiesByState():
    """[citiesByState method]

    Returns:
        [html]: [fetches html page]
    """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
