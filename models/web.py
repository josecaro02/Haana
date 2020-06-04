#!/usr/bin/python3
import mongoengine as me


class Web(me.EmbeddedDocument):
    logo = me.StringField()
    color = me.StringField()
    background = me.StringField()
