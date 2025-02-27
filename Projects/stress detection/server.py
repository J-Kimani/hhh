from flask import Flask, request, jsonify
import requests
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return 'Hello'

@app.route("/stress", methods= ["GET", "POST"])
def stress_pred():
    user = str(request.form['user'])

    response = jsonify({
        "St": util.det_stress(user)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Server")
    util.load()
    app.run()