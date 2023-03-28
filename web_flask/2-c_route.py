#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohnbn():
    name = request.args.get("name", "Hello HBNB!")
    return name


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    name = request.args.get("name", "HBNB")
    return name


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def C_OP(text):
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
