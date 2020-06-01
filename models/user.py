#!/usr/bin/python3
from datetime import datetime
import mongoengine as me


class Users(me.Document):
    created_at = me.DateTimeField(default=datetime.now())
    name = me.StringField(required=True)
    type = me.StringField()
    email = me.StringField()
    passwd = me.StringField()
    phone = me.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
