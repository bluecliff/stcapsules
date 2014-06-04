#!/usr/bin/env python
# encoding: utf-8

from core import db
import datetime
from user import User
from mongoengine import StringField,ReferenceField,DateTimeField,ListField,EmbeddedDocumentField,PointField,IntField

PERMISSIONS={'PUBLIC':0,
             'PROTECTED':1,
             'PRIVATE':2,
        }

class Post(db.Document):
    @property
    def id(self):
        return str(self.pk)

    author=ReferenceField(User)
    location=PointField(required=True)
    distance=IntField(required=True)
    created_at=DateTimeField(default=datetime.datetime.utcnow,required=True)
    active_time=DateTimeField(required=True)
    permission=IntField(required=True,default=PERMISSIONS['PUBLIC'])
    followers=IntField(required=True,default=0)
    content=StringField(required=True)
    image=StringField(max_length=1024)
    wavefield=StringField(max_length=1024)
    comments=ListField(EmbeddedDocumentField('Comment'))

    meta={
            'ordering':['-created_at']
            }

class Comment(EmbeddedDocumentField):
    created_at=DateTimeField(default=datetime.datetime.utcnow,required=True)
    content=StringField(required=True)
    author=ReferenceField(User,required=True)
    meta={
            'ordering':['-created_at']
            }
