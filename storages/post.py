#!/usr/bin/env python
# encoding: utf-8

from core import db
import datetime
from user import User
from mongoengine import Document,StringField,URLField,ReferenceField,DateTimeField,ListField,GeoPointField,IntField

CATEGORY={'PUBLIC':0,
          'PROTECTED':1,
          'PRIVATE':2,
          'ADS':3,
        }
DISTANCE=[50,200,1000,5000]


class Post(Document):
    @property
    def id(self):
        return str(self.pk)

    author=ReferenceField(User)
    title=StringField(required=True,max_length=20)
    location=GeoPointField(required=True)
    location_name=StringField(max_length=512)
    distance=IntField(required=True,default=DISTANCE[0])
    created_at=DateTimeField(default=datetime.datetime.utcnow,required=True)
    active_time=DateTimeField(required=True)
    category=IntField(required=True,default=CATEGORY['PUBLIC'])
    followers=ListField(ReferenceField(User))
    receivers=ListField(ReferenceField(User))
    content=StringField(required=True)
    imagekey=StringField()
    wavekey=StringField()

    meta={
            'ordering':['-active_time']
            }

