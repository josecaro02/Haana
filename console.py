#!/usr/bin/python3
""" HAANNA console """
import cmd
import models.mongo_setup as mongo_setup
import services.data_service as svc
import infraestructure.state as state
import json
import shlex
from models.user import Users, UserExists
from models.reviews import Reviews
from models.stores import Stores

classes = {'Users': Users, 'Reviews': Reviews, 'Stores': Stores}

class HAANACommand(cmd.Cmd):
	""" HANNACommand class """

	mongo_setup.global_init()
	prompt = "(haana) "

	def do_quit(self, line):
		""" quit command """
		return True

	def do_EOF(self, line):
		""" EOF command """
		return True

	def emptyline(self):
		""" emptyline """
		pass

	def do_log(self, line):
		""" Logg in to the app """
		data = line.split()
		email = data[0]
		account = svc.find_account(email)
		if not account:
			print(f"Could not fin account with email {email}")
			return
		state.active_account = account
		print("Logged in Succesfully.")

	def do_make_review(self, line):
		""" Reviews make by the user for the store
			this function receives a JSON"""
		if not state.active_account:
			print("You must login first to register a review.")
		else:
			line1 = json.loads(line)
			for key, value in line1.items():
				if (key == "store_id"):
					store_id = value
				if (key == "description"):
					description = value
				if (key == "score"):
					score = value
			user_id = state.active_account.id
			svc.write_review(store_id, user_id, description, score)
			print("Review saved correctly")

	def do_list_reviews(self, line):
		""" Recives one argument: store_id """
		reviews = svc.show_reviews(line)
		print(reviews)

	def do_list_store(self, line):
		""" Recives two arguments type of store
			and the location"""
		line1 = json.loads(line)
		for key, value in line1.items():
			if (key == "type"):
				type_store = value
			if (key == "location"):
				location = value
		store = svc.show_stores(type_store, location)
		print(store)

	def do_add_product(self, line):
		""" Add a producto to an store, recieving an JSON
		with an store _id and producto info (name, value,
		description and img_link) """
		line1 = json.loads(line)
		for key, value in line1.items():
			if (key == "_id"):
				_id = value
			if (key == "name"):
				name = value
			if (key == "value"):
				value = value
			if (key == "description"):
				description = value
			if (key == "img_link"):
				img_link = value
		new_product = svc.add_product(_id, name, value, description, img_link)
		print(new_product)

	def do_update_prod(self, line):
		svc.update_product()
		svc.create_product()

	def do_create(self, line):
		args = line.split()
		if len(line) == 0:
			print("Class missing")
			return
		if args[0] in classes:
			new_dict = self._key_value_parser(args[1:])
			instance = classes[args[0]](**new_dict)
		else:
			print("* class doesn't exist *")
			return False
		try:
			instance.save()
			print(instance.to_json())
		except UserExists:
			print("Email already used!!")
			del instance

	def _key_value_parser(self, args):
		"""creates a dictionary from a list of strings"""
		new_dict = {}
		for arg in args:
			if "=" in arg:
				kvp = arg.split('=', 1)
				key = kvp[0]
				value = kvp[1]
				if value[0] == value[-1] == '"':
					value = shlex.split(value)[0].replace('_', ' ')
				else:
					try:
						value = int(value)
					except:
						try:
							value = float(value)
						except:
							continue
				new_dict[key] = value
		return new_dict


if __name__ == '__main__':
	HAANACommand().cmdloop()
