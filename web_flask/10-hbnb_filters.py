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


@app.route('/hbnb_filters', strict_slashes=False)
def StatesAndcitiesByState():
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)