#!/usr/bin/python3
import datetime
import mongoengine as me
from models import Locations, Product, Web


class Stores(me.Document):
    created_at = me.DateTimeField(default=datetime.now)
    name = me.StringField(required=True)
    phone = me.StringFIeld(require=True)
    type = me.StringField(required=True)
    sub_type = me.StringField(required=True)
    is_active = me.BooleanField(required=True)
    location = me.EmbeddedDocumentListField(Locations)
    owner_id = me.ListField()
    products = me.EmbeddedDocumentListField(Product)
    web_info = me.EmbeddedDocumentListField(Web)
    meta = {
        'db_alias': 'core',
        'collection': 'stores'
    }
