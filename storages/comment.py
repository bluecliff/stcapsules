#!/usr/bin/env python
# encoding: utf-8

from core import db
from mongoengine import Document,StringField,DateTimeField,ReferenceField
import datetime
from user import User
from post import Post

class Comment(Document):
    author=ReferenceField(User,required=True)
    post=ReferenceField(Post,required=True)
    content=StringField(max_length=1024,required=True)
    created_at=DateTimeField(default=datetime.datetime.utcnow())

    meta={
        'ordering':['-created_at']
        }
