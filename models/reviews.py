#!/usr/bin/python3
from datetime import datetime
import mongoengine as me


class Reviews(me.Document):
    created_at = me.DateTimeField(default=datetime.now())
    store_id = me.StringField()
    user_id = me.StringField()
    description = me.StringField()
    score = me.IntField(min_value=0, max_value=5)
    meta = {
        'db_alias': 'core',
        'collection': 'reviews'
    }
