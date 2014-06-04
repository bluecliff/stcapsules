#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,marshal,fields
from utils import authenticated
from base import BaseArgs,UserField
from models.post import add_post

class PostPostArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('title',type=str,help='title must be string')
        self.parser.add_argument('longitude',type=float,help='longtitude must be float')
        self.parser.add_argument('latitude',type=float,help='latitude must be float')
        self.parser.add_argument('distance',type=int,help='distance have to be integer')
        self.parser.add_argument('active_time',type=int,help='active_time must be an timedate type')
        self.parser.add_argument('category',type=int,help='category have to be integer')
        self.parser.add_argument('content',type=str)
        self.parser.add_argument('imageurl',type=str)
        self.parser.add_argument('waveurl',type=str)
        self.parser.add_argument('receivers',type=str,action='append')

post_fields={
        'id':fields.String,
        'title':fields.String,
        'author':UserField,
        }

class PostResource(Resource):
    @authenticated()
    def post(self):
        """add an new item to Post collection"""
        args=PostPostArgs().args
        return marshal(add_post(**args),post_fields)
