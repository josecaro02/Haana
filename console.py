#!/usr/bin/python3
""" HAANNA console """
import cmd
import models.mongo_setup as mongo_setup
import services.data_service as svc
import infraestructure.state as state


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


if __name__ == '__main__':
    HAANACommand().cmdloop()
