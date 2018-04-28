#Needs flask, flask-pymongo
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient

#intializes MongoDB
client = MongoClient('localhost', 27017)
#select database
db = client.directory
#select collection within that database
collection = db.inventory
# def create_app():
app = Flask(__name__)


#@app.route("/getWorkers")
@app.route("/")
def get_worker():
    #get the object based on search parameter without id
    collection_list = collection.find({"status": "true"}, {"_id": False})
    #move entries from cursor
    worker_list = []
    for worker in collection_list:
    	worker = jsonify(worker)
    	worker_list.append(worker)

    return worker_list[0]

    