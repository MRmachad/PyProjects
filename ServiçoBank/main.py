from flask import Flask, request, jsonify
from bibs.bd import BD
from bibs.hold import Holder

app = Flask(__name__)

bd = BD()
hold = Holder()

@app.route("/")
def hello():
    return "<h1>Hello Worlllllaaaaaaaaaaasdfafaaad! </h1>"

@app.route('/envio', methods=['POST'])
def webhook():

    data = request.get_json(force=True)
    print(data)

    return "OK", 200

if __name__ == '__main__':

    app.run("0.0.0.0", 3060, debug = True)
