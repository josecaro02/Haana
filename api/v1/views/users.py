#!/usr/bin/python3
""" Stores API """

from api.v1.app import mongo
from api.v1.views import app_views
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request

def validate_user(data_user):
    required = ['name', 'email', 'passwd', 'type']
    for field in required:
        if field not in data_user:
            return False
    return True

def created_user(user_email):
    user = mongo.db.users.find_one({"email": user_email})
    print(user, user_email)
    return True if user else False

@app_views.route('/users', methods=['GET'])
def get_users():
    users_list = mongo.db.users.find()
    user = []
    for one_user in users_list:
        one_user['_id'] = str(one_user['_id'])
        user.append(one_user)
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        abort(404)
    user['_id'] = str(user['_id'])
    return make_response(jsonify(user), 200)

@app_views.route('/users', methods=['POST'])
def post_user():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if not validate_user(data):
        abort(400, description="Bad JSON: Some required field is missing")
    if created_user(data['email']):
        abort(409, description="Email already used")
    user_id = mongo.db.users.insert(data)
    user = mongo.db.users.find_one({"_id": user_id})
    user['_id'] = str(user['_id'])
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        abort(404)
    if 'email' in data:
        data_email = data['email']
        if created_user(data_email) and user['email'] != data_email:
            abort(409, description="Email already used")
    for key, item in data.items():
        mongo.db.users.update_one({"_id": ObjectId(user_id)},
                                       {'$set': {key: item}})
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    user['_id'] = str(user['_id'])
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        abort(404)
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    user['_id'] = str(user['_id'])
    return make_response(jsonify(user), 200)
