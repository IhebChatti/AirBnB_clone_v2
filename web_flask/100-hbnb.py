#!/usr/bin/python3
"""[python script that starts a Flask web application]
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """[teardown method]
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def StatesAndcitiesByState():
    """[statesand cities by state]

    Returns:
        [html]: [fetches html page]
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
