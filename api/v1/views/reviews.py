#!/usr/bin/python3
""" Stores API """

from api.v1.app import mongo
from api.v1.views import app_views
from bson.objectid import ObjectId
from datetime import datetime
from flask import abort, jsonify, make_response, request

def validate_review(data_review):
    required = ['store_id', 'user_id', 'score']
    for field in required:
        if field not in data_review:
            return False
    data_review['user_id'] = ObjectId(data_review['user_id']) 
    return True

@app_views.route('/stores/<store_id>/reviews', methods=['GET'])
def get_reviews_by_store(store_id):
    store = mongo.db.stores.find({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    reviews_list = mongo.db.reviews.find({'store_id': ObjectId(store_id)})
    review = []
    for one_review in reviews_list:
        one_review['_id'] = str(one_review['_id'])
        one_review['store_id'] = str(one_review['store_id'])
        one_review['user_id'] = str(one_review['user_id'])
        review.append(one_review)
    return make_response(jsonify(review), 200)

@app_views.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    user = mongo.db.users.find({'_id': ObjectId(user_id)})
    if not user:
        abort(404)
    reviews_list = mongo.db.reviews.find({'user_id': ObjectId(user_id)})
    review = []
    for one_review in reviews_list:
        one_review['_id'] = str(one_review['_id'])
        one_review['store_id'] = str(one_review['store_id'])
        one_review['user_id'] = str(one_review['user_id'])
        review.append(one_review)
    return make_response(jsonify(review), 200)

@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if not review:
        abort(404)
    review['_id'] = str(review['_id'])
    review['store_id'] = str(review['store_id'])
    review['user_id'] = str(review['user_id'])
    return make_response(jsonify(review), 200)

@app_views.route('/stores/<store_id>/reviews', methods=['POST'])
def post_review(store_id):
    store = mongo.db.stores.find_one({'_id': ObjectId(store_id)})
    if not store:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    data['store_id'] = ObjectId(store_id) 
    if not validate_review(data):
        abort(400, description="Bad JSON: Some required field is missing")
    user = mongo.db.users.find_one({'_id': ObjectId(data['user_id'])})
    if not user:
        abort(404)
    if user['_id'] == store['owner_id']:
        abort(409, description='Owner cannot make a review of its own restaurant')
    user_review_of_store = mongo.db.reviews.find_one({'user_id': user['_id'],
                                                      'store_id': store['_id']})
    if user_review_of_store:
        abort(409, description='User already made a review of this resaturant')
    data['created_at'] = datetime.isoformat(datetime.utcnow())
    review_id = mongo.db.reviews.insert(data)
    review = mongo.db.reviews.find_one({"_id": review_id})
    review['_id'] = str(review['_id'])
    review['store_id'] = str(review['store_id'])
    review['user_id'] = str(review['user_id'])
    return make_response(jsonify(review), 200)

@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if not review:
        abort(404)
    if 'user_id' in data or 'store_id' in data:
        abort(409, "Cannot change user or store")
    for key, item in data.items():
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)},
                                       {'$set': {key: item}})
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    review['_id'] = str(review['_id'])
    review['store_id'] = str(review['store_id'])
    review['user_id'] = str(review['user_id'])
    return make_response(jsonify(review), 200)

@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if not review:
        abort(404)
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    review['_id'] = str(review['_id'])
    review['store_id'] = str(review['store_id'])
    review['user_id'] = str(review['user_id'])
    return make_response(jsonify(review), 200)
