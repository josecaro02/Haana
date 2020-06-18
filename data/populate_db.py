#!/usr/bin/python3

import csv
import bcrypt
import pymongo
from datetime import datetime

def get_all_products(products_file):
	with open(products_file, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		return list(dict(prod) for prod in csv_reader)

def insert_users(users_file):
	with open(users_file, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line = 0
		error = 0
		for user in csv_reader:
			if db.users.find_one({'email': user['email']}):
				print("Couldn't add {}: reapeted email".format(user['name']))
				error += 1
			else:
				user['passwd'] = bcrypt.hashpw(user['passwd'].encode(), bcrypt.gensalt()).decode()
				user['created_at'] = datetime.isoformat(datetime.utcnow())
				db.users.insert_one(user)
				line += 1
	print("Added {:d} users{}".format(line, '' if error == 0 else f' rejected {error} users'))

def insert_stores(stores_file, products_file):
	products = get_all_products(products_file)
	with open(stores_file, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line = 0
		error = 0
		for row in csv_reader:
			store = dict(row)
			user_email = store.pop('owner')
			user = db.users.find_one({'email': user_email})
			if not user:
				print("Could not find a user with email {}".format(user_email))
				error += 1
			elif user['type'] != 'owner':
				print("User {}({}) is a {}".format(user['name'], user['email'], user['type']))
				error += 1
			else:
				store['owner_id'] = user['_id']
				store['created_at'] = datetime.isoformat(datetime.utcnow())
				store['location'] = {'city': store.pop('city')}
				store['web_info'] = {'logo': store['web_info']}
				store['products'] = list(filter(lambda prod: prod['store'] == store['name'], products))
				db.stores.insert_one(store)
				line += 1
				print("\tAdded {:d} products for {}".format(len(store['products']), store['name']))
	print("Added {:d} stores{}".format(line, '' if error == 0 else f'rejected {error} stores'))

if __name__ == "__main__":
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient["co_haana"]
	db.users.drop()
	insert_users('data/data_users.csv')
	db.stores.drop()
	insert_stores('data/data_stores.csv', 'data/data_products.csv')
