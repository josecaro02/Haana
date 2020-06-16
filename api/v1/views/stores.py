#!/usr/bin/python3
''' Stores API '''

from api.v1.views import app_views
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request
from models import mongo_db

def validate_store(data_store):
    required = ['name', 'phone', 'type', 'sub_type', 'schedule', 'location', 'owner_id']
    for field in required:
        if field not in data_store:
            return False
    return True

@app_views.route('/stores', methods=['GET'])
def get_stores():
    stores_list = mongo_db.stores.find()
    store = []
    for one_store in stores_list:
        one_store['_id'] = str(one_store['_id'])
        one_store['owner_id'] = str(one_store['owner_id'])
        store.append(one_store)
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>', methods=['GET'])
def get_store(store_id):
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    store['_id'] = str(store['_id'])
    store['owner_id'] = str(store['owner_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/users/<user_id>/stores', methods=['GET'])
def get_stores_by_user(user_id):
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    if not user or user['type'] != 'owner':
        abort(404)
    stores_db = mongo_db.stores.find({'owner_id': user['_id']})
    stores_user = []
    for store in stores_db:
        store['_id'] = str(store['_id'])
        store['owner_id'] = str(store['owner_id'])
        stores_user.append(store)
    return make_response(jsonify(stores_user), 200)

@app_views.route('/stores/<store_id>/products', methods=['GET'])
def get_store_products(store_id):
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    return make_response(jsonify(store['products']), 200)

@app_views.route('/location/<city>', methods=['GET'])
def get_store_by_city(city):
    city = city.lower()
    stores_list = mongo.db.stores.find({'location': {'city': city}})
    store = []
    for one_store in stores_list:
        one_store['_id'] = str(one_store['_id'])
        one_store['owner_id'] = str(one_store['owner_id'])
        store.append(one_store)
    return make_response(jsonify(store), 200)

@app_views.route('/users/<user_id>/stores', methods=['POST'])
def post_store(user_id):
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    if not user or user['type'] != 'owner':
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    data['owner_id'] = ObjectId(user_id)
    if not validate_store(data):
        abort(400, description='Bad JSON: Some required field is missing')
    data['created_at'] = datetime.isoformat(datetime.utcnow())
    store_id = mongo_db.stores.insert(data)
    store = mongo_db.stores.find_one({'_id': store_id})
    store['_id'] = str(store['_id'])
    store['owner_id'] = str(store['owner_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>', methods=['PUT'])
def update_store(store_id):
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    for key, item in data.items():
        mongo_db.stores.update_one({'_id': ObjectId(store_id)},
                                   {'$set': {key: item}})
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    store['_id'] = str(store['_id'])
    store['owner_id'] = str(store['owner_id'])
    return make_response(jsonify(store), 200)

@app_views.route('/stores/<store_id>/products', methods=['POST'])
def add_store_products(store_id):
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    final_products = store["products"] + data
    mongo_db.stores.update_one({'_id': ObjectId(store_id)},
                               {'$set': {"products": final_products}})
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    return make_response(jsonify(store["products"]), 200)

@app_views.route('/stores/<store_id>/products', methods=['DELETE'])
def delete_store_products(store_id):
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    products = store["products"]
    for product in products:
        for product_to_delete in data:
            if product["name"] == product_to_delete["name"]:
                products.remove(product)
    mongo_db.stores.update_one({'_id': ObjectId(store_id)},
                               {'$set': {"products": products}})
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    return make_response(jsonify(store["products"]), 200)

@app_views.route('/stores/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    store = mongo_db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    mongo_db.stores.remove({'_id': ObjectId(store_id)})
    store['_id'] = str(store['_id'])
    store['owner_id'] = str(store['owner_id'])
    return make_response(jsonify(store), 200)
