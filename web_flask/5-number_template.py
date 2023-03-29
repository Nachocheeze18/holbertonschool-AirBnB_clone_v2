#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohnbn():
    name = request.args.get("name", "Hello HBNB!")
    return name


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    name = request.args.get("name", "HBNB")
    return name


@app.route('/python/', defaults={'text': 'is cool'},
           methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def C_OP(text):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def ints(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def ints_n_temps(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
