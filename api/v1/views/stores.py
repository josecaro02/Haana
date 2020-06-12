#!/usr/bin/python3
""" Stores API """

from api.v1.app import mongo
from api.v1.views import app_views
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request

def validate_store(data_store):
    required = ['name', 'phone', 'type', 'sub_type', 'schedule', 'location', 'owner_id']
    for field in required:
        if field not in data_store:
            return False
    return True

@app_views.route('/stores', methods=['GET'])
def get_stores():
    stores_list = mongo.db.stores.find()
    store = []
    for one_store in stores_list:
        one_store['_id'] = str(one_store['_id'])
        store.append(one_store)
    print("hello")
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>', methods=['GET'])
def get_one_store(store_id):
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    if not store:
        abort(404)
    store['_id'] = str(store['_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>/products', methods=['GET'])
def get_one_store_products(store_id):
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    if not store:
        abort(404)
    return make_response(jsonify(store['products']), 200)

@app_views.route('/stores', methods=['POST'])
def post_store():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if not validate_store(data):
        abort(400, description="Bad JSON: Some required field is missing")
    store_id = str(mongo.db.stores.insert(data))
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    store['_id'] = str(store['_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>', methods=['PUT'])
def update_store(store_id):
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    if not store:
        abort(404)
    for key, item in data.items():
        mongo.db.stores.update_one({"_id": ObjectId(store_id)},
                                       {'$set': {key: item}})
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    store['_id'] = str(store['_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    if not store:
        abort(404)
    mongo.db.stores.remove({'_id': ObjectId(store_id)})
    store['_id'] = str(store['_id'])
    return make_response(jsonify(store), 200)
