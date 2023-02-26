import model_old as model








from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root(): return


@app.route("/api")
def hello():
    items = [
        'tomato',
        'maize',
        'plaintain',
        'potatoes',
        'rice',
        'mustard',
        'soybeans',
        'sweet potatoes',
        'wheat',
        'onion'
    ]

    temp, rainfall = [x.split("=")[-1][:-1] for x in open('VARS').readlines()]
    # print (temp, rainfall)
    # print(dict(zip(items, model.calc_for_everything(temp, rainfall, items))))
    return jsonify(dict(zip(items, model.calc_for_everything(temp, rainfall, items))))

if __name__ == '__main__':
    app.run(port=3636)
