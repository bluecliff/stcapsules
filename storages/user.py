#!/usr/bin/env python
# encoding: utf-8

from core import db
import datetime
from mongoengine import Document,StringField,ListField,ReferenceField,DateTimeField


class User(Document):
    @property
    def id(self):
        return str(self.pk)

    user_id=StringField(max_length=256,unique=True,required=True)
    created_at=DateTimeField(default=datetime.datetime.utcnow,required=True)
