#!/usr/bin/python3
''' Authentication module '''

from api.v1.app import bcrypt
from api.v1.auth import app_auth
from bson.objectid import ObjectId
from flask import abort, jsonify, make_response, request
from functools import wraps
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
        payload = {'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                   'iat': datetime.datetime.utcnow(),
                   'email': user['email'],
                   'user_id': str(user['_id'])}
        token = jwt.encode(payload, 'haana', algorithm='HS256')
        info = {'status': 'login succesful',
                'auth_token': token.decode()}
        resp = make_response(jsonify(info))
        resp.set_cookie('auth_token', token.decode())
        return resp
    else:
        abort(403, description="Invalid user or password")

def get_token():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        if 'Bearer ' in auth_header and len(auth_header.split(' ')) == 2:
            return auth_header.split(' ')[1]
        else:
            abort(401, description="Bearer token malformed")
    else:
        abort(401, description="Authorization required")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = get_token()
        try:
            payload = jwt.decode(auth_token, 'haana')
        except jwt.ExpiredSignatureError:
            abort(401, descripton="Signature expired")
        except jwt.InvalidTokenError:
            abort(401, description="Invalid token")
        if f.__name__ == 'get_user_info':
            payload.pop('iat')
            payload.pop('exp')
            return make_response(jsonify(payload))
        return f(*args, **kwargs)
    return decorated_function

@app_auth.route('/user')
@login_required
def get_user_info():
    pass
