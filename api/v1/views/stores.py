#!/usr/bin/python3
""" Stores API """

from api.v1.app import mongo
from api.v1.views import app_views
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request


@app_views.route('/stores', methods=['GET'])
def get_stores():
    stores_list = mongo.db.stores.find()
    store = []
    for one_store in stores_list:
        one_store['_id'] = str(one_store['_id'])
        store.append(one_store)
    print("hello")
    return jsonify(store)


@app_views.route('/stores/<store_id>', methods=['GET'])
def get_one_store(store_id):
    store = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    return jsonify(store)


@app_views.route('/stores/<store_id>/<name>', methods=['DELETE'])
def delete_product(store_id, name):
    stores_list = mongo.db.stores.find_one({"_id": ObjectId(store_id)})
    products = stores_list['products']
    for product in products:
        if product['name'] == name:
            products.remove(product)
    mongo.db.stores.update_one({"_id": ObjectId(store_id)},
                               {'$set': {'products': products}})
    return jsonify(None)
