#!/usr/bin/python3
''' Stores API '''

from api.v1.app import bcrypt
from api.v1.views import app_views
from api.v1.auth.access import *
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request
from models import mongo_db

def validate_user(data_user):
    required = ['name', 'email', 'passwd', 'type']
    for field in required:
        if field not in data_user:
            return False
    return True

def created_user(user_email):
    user = mongo_db.users.find_one({'email': user_email})
    return True if user else False

@app_views.route('/users', methods=['GET'])
def get_users():
    users_list = mongo_db.users.find()
    user = []
    for one_user in users_list:
        one_user['_id'] = str(one_user['_id'])
        one_user.pop('passwd')
        user.append(one_user)
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    if not user:
        abort(404)
    user['_id'] = str(user['_id'])
    user.pop('passwd')
    return make_response(jsonify(user), 200)

@app_views.route('/users', methods=['POST'])
def post_user():
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    if not validate_user(data):
        abort(400, description='Bad JSON: Some required field is missing')
    if created_user(data['email']):
        abort(409, description='Email already exists. Please Log in')
    data['passwd'] = bcrypt.generate_password_hash(data['passwd']).decode()
    user_id = mongo_db.users.insert(data)
    user = mongo_db.users.find_one({'_id': user_id})
    user['_id'] = str(user['_id'])
    user.pop('passwd')
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.get_json()
    if not data:
        abort(400, description='Not a JSON')
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    if not user:
        abort(404)
    if 'email' in data:
        data_email = data['email']
        if created_user(data_email) and user['email'] != data_email:
            abort(409, description='Email already used')
    for key, item in data.items():
        if key == 'passwd':
            item = bcrypt.generate_password_hash(item).decode()
        mongo_db.users.update_one({'_id': ObjectId(user_id)},
                                       {'$set': {key: item}})
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    user['_id'] = str(user['_id'])
    user.pop('passwd')
    return make_response(jsonify(user), 200)

@app_views.route('/users/<user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = mongo_db.users.find_one({'_id': ObjectId(user_id)})
    if not user:
        abort(404)
    mongo_db.users.remove({'_id': ObjectId(user_id)})
    user['_id'] = str(user['_id'])
    user.pop('passwd')
    return make_response(jsonify(user), 200)
