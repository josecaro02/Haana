#!/usr/bin/python3
''' Authentication module '''

from api.v1.app import bcrypt
from api.v1.auth import app_auth
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request
from models import mongo_db
import datetime
import jwt


@app_auth.route('/', methods=['POST'])
def user_login():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if not ('email' in data and 'passwd' in data):
        abort(400, description="Not enough information")
    user = mongo_db.users.find_one({'email': data["email"]})
    if user and bcrypt.check_password_hash(user['passwd'], data['passwd']):
        payload = {'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
                   'iat': datetime.datetime.utcnow(),
                   'email': user['email']}
        token = jwt.encode(payload, 'haana', algorithm='HS256')
        info = {'status': 'login succesful',
                'auth_token': token.decode()}
        return make_response(jsonify(info), 200)
    else:
        abort(403, description="Invalid user or password")
