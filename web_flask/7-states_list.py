#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    all_obj = storage.all(State)
    return render_template('7-states_list.html', states=all_obj)


@app.teardown_appcontext
def teardown_context_session(self):
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
