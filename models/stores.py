#!/usr/bin/python3
from datetime import datetime
import mongoengine as me
from models.locations import Locations
from models.product import Product
from models.web import Web


class Stores(me.Document):
    created_at = me.DateTimeField(default=datetime.now())
    name = me.StringField(required=True)
    phone = me.StringField(require=True)
    type = me.StringField(required=True)
    sub_type = me.StringField(required=True)
    is_active = me.BooleanField(required=True)
    location = me.MapField(me.EmbeddedDocumentListField(Locations))
    owner_id = me.StringField()
    products = me.MapField(me.EmbeddedDocumentListField(Product))
    web_info = me.MapField(me.EmbeddedDocumentListField(Web))
    schedule = me.StringField()
    meta = {
        'db_alias': 'core',
        'collection': 'stores'
    }
