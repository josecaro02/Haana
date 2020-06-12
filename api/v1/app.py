#!/usr/bin/python3
""" Flask - PyMongo App """

from flask import Flask, request, jsonify, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from api.v1.views import app_views

app = Flask("__name__")
app.url_map.strict_slashes = False

app.config["MONGO_DBNAME"] = "co_haana"
app.config["MONGO_URI"] = "mongodb://localhost:27017/co_haana"

app.register_blueprint(app_views)
mongo = PyMongo(app)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_fount(error):
    """ 404 error """
    return make_response(jsonify())



if __name__ == "__main__":
    app.run(port = "5000", debug=True)
