#Needs flask, flask-pymongo
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from pymongo import MongoClient


#intializes MongoDB
client = MongoClient("mongodb+srv://hackathon2018:Shantanu123$%^@nyuadwadhafni2018-sjngs.mongodb.net/test")
#select database
db = client.directory
#select collection within that database
collection = db.inventory
# def create_app():
app = Flask(__name__)


@app.route("/getWorkers", methods=['GET', 'POST'])
def get_worker():
	req_location = request.args.get('loc')
	req_skill = request.args.get('skill')
	req_language = request.args.get('lang')
	collection_list = collection.find({"skill": req_skill, "loc": req_location, "status": "true", "language": req_language}, {"_id": False})
	worker_list = []
	count = 0
	for worker in collection_list:
		worker = jsonify(worker)
		worker_list.append(worker)
		count = count + 1

	return worker_list[0]

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)