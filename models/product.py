#!/usr/bin/python3
import mongoengine as me
from models import Details


class Product(me.EmbeddedDocument):
    name = me.EmbeddedDocument(Details)
