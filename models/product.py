#!/usr/bin/python3
import mongoengine as me


class Product(me.EmbeddedDocument):
    name = me.StringField()
    value = me.StringField()
    description = me.StringField()
    link = me.StringField()
