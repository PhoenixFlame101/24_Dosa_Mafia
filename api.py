# flask_ngrok_example.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root(): return


@app.route("/api")
def hello():
    items = ["Potato", "Tomato"]
    prices = [123, 256]
    return jsonify(dict(zip(items, prices)))


if __name__ == '__main__':
    app.run()
