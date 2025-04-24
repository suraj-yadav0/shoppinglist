from random import randrange

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/itemprice")
def itemprice():
    return {"name": request.args.get("itemname"), "price": randrange(1000) / 100}