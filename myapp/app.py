#Needs flask, flask-pymongo
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.json_util import dumps, loads

#intializes MongoDB
client = MongoClient('localhost', 27017)
#select database
db = client.directory
#select collection within that database
collection = db.inventory
# def create_app():
app = Flask(__name__)


#def hello_world():
  #  return "hello world"

#@app.route("/getWorkers")
@app.route("/")
def get_worker():
    #get the object based on search parameter
    collection_list = collection.find({"status": "true"}, {"_id": False})
    worker_list = []
    for worker in collection_list:
    	worker_list.append(worker)

    return jsonify(worker_list[0])
    #return some info of the search result
    