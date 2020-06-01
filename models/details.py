#!/usr/bin/python3
import mongoengine as me


class Details(me.EmbeddedDocument):
    value = me.StringField()
    description = me.StringField()
    link = me.StringField()
