#!/usr/bin/python3
from datetime import datetime
import mongoengine as me


class UserExists(Exception):
    pass

class Users(me.Document):
    created_at = me.DateTimeField(default=datetime.now())
    name = me.StringField(required=True)
    type = me.StringField()
    email = me.EmailField()
    passwd = me.StringField()
    phone = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }


    def save(self):
        user = Users.objects(email=self.email).first()
        if user:
            raise UserExists
        super().save()
