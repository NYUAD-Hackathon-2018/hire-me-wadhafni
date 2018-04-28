from flask import Flask, jsonify


person1 = {"phone": "888888", "name":"nyu", "loc": "dubai", "skill":"bakery"}
data = [person1]

# def create_app():
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/getWorkers")
def get_worker():
    return jsonify(data)