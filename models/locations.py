#!/usr/bin/python3
import mongoengine as me


class Locations(me.EmbeddedDocument):
    department = me.StringField(Required=True)
    city = me.StringField(required=True)
    address = me.StringField(required=True)
    pin = me.StringField()
