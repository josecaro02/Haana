#!/usr/bin/python3
''' Authentication module '''

from api.v1.auth import app_auth
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request
from models import mongo_db

@app_auth.route('/', methods=['POST'])
def user_login():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if not ('email' in data and 'passwd' in data):
        abort(400, description="Not enough information")
    user = mongo_db.users.find_one({'email': data["email"]})
    if user and user['passwd'] == data['passwd']:
        info = {'status': 'login succesful'}
        return make_response(jsonify(info), 200)
    else:
        abort(403, description="Invalid user or password")

