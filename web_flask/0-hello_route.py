#!/usr/bin/python3
<<<<<<< HEAD
""" scripts start a web app to listen on 0.0.0.0 port 5000. """

=======
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
>>>>>>> 57843285ea2be9cf8fce55cd1bc6ca18c5afbf81
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns 'Hello HBNB!' to the output"""
=======
@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
>>>>>>> 57843285ea2be9cf8fce55cd1bc6ca18c5afbf81
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run(host="0.0.0.0")
>>>>>>> 57843285ea2be9cf8fce55cd1bc6ca18c5afbf81
