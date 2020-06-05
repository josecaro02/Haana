#!/usr/bin/python3
""" HAANNA console """
import cmd
import models.mongo_setup as mongo_setup
import services.data_service as svc
import infraestructure.state as state
import json


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

    def do_create_account(self, line):
        """ Create command"""
        my_list = line.split()
        name = my_list[0]
        email = my_list[1]
        passwd = my_list[2]
        check_account = svc.find_account(email)
        if check_account:
            print(f"ERROR: Account with email {email} already exists")
        else:
            state.active_account = svc.create_account(name, email, passwd)
            print(f"Created new account with id {state.active_account.id}.")

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


    def do_create_store(self, line):
        line1 = json.loads(line)
        for key, value in line1.items():
            if (key == 'location'):
                location = value
            if (key == 'name'):
                name = value
            if (key == 'phone'):
                phone = value
            if (key == 'type'):
                type_ = value
            if (key == 'sub_type'):
                subtype = value
            if (key == 'owner_id'):
                owner_id = value
            if (key == 'web_info'):
                web_info = value
        new_store = svc.create_store(name, phone, type_, subtype
                                     , owner_id)
        print(new_store)

    def do_update_prod(self, line):
        svc.update_product()
        svc.create_product()
if __name__ == '__main__':
    HAANACommand().cmdloop()
