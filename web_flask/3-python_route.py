#!/usr/bin/python3
"""
    comentario
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Connect_path1():
    """ Comentario
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def Connect_path2():
    """ Comentario
    """
    return 'HBNB'


@app.route("/c/<string:text>", strict_slashes=False)
def Connect_path3(text):
    """ Comentario
    """
    return "C %s" % text.replace('_', ' ')


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<string:text>", strict_slashes=False)
def Connect_path4(text):
    """ Comentario
    """
    return "Python %s" % text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
