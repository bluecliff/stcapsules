#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,marshal
from base import BaseArgs,UserField,LocationField,LengthField
from utils import authenticated
from models.user_post_relation import get_receives
from config import DEFAULT_ITEMS

class ReceiveQueryArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('start',type=int,default=0)
        self.parser.add_argument('end',type=int,default=DEFAULT_ITEMS)

receive_fields={
        'id':fields.String,
        'author':UserField,
        'title':fields.String,
        'location':LocationField,
        'active_time':fields.DateTime,
        'category':fields.Integer,
        'followers':LengthField,
        }

class ReceiveResource(Resource):
    @authenticated()
    def get(self):
        args=ReceiveQueryArgs().args
        return marshal(get_receives(**args),receive_fields)
