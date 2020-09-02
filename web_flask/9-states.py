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


@app.route('/states', strict_slashes=False)
def citiesByState():
    """[citiesByState method]

    Returns:
        [html]: [fetches html page]
    """
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def statesId(id):
    """[statesID method]

    Args:
        id ([str]): [state id]

    Returns:
        [html]: [fetches html page]
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', state=state)
        return render_template("9-states.html", state=state)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
