#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def startup():
    name = request.args.get("name", "Hello HBNB!")
    return name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
