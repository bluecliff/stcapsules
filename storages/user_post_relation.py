#!/usr/bin/env python
# encoding: utf-8

from core import db
from mongoengine import Document,ListField,ReferenceField
from user import User
from post import Post

class User_Post_Relation(Document):
    """a many to many relation between user an post"""
    @property
    def id(self):
        return str(self.pk)
    user=ReferenceField(User,unique=True)
    receives=ListField(ReferenceField(Post))
    favourites=ListField(ReferenceField(Post))
