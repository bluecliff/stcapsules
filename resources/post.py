#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,marshal,fields
from utils import authenticated
from base import BaseArgs,UserField,LocationField,LengthField,KeyURLField
from models.post import add_post,get_post,get_post_list

class PostListPostArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('title',type=unicode,help='title must be string')
        self.parser.add_argument('longitude',type=float,help='longtitude must be float')
        self.parser.add_argument('latitude',type=float,help='latitude must be float')
        self.parser.add_argument('distance',type=int,help='distance have to be integer')
        self.parser.add_argument('active_time',type=float,help='active_time must be an timedate type')
        self.parser.add_argument('category',type=int,help='category have to be integer')
        self.parser.add_argument('content',type=unicode)
        self.parser.add_argument('imagekey',type=unicode)
        self.parser.add_argument('wavekey',type=unicode)
        self.parser.add_argument('receivers',type=unicode,action='append')

class PostListQueryArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('start',type=int)
        self.parser.add_argument('end',type=int)
        self.parser.add_argument('longitude',type=float)
        self.parser.add_argument('latitude',type=float)

class PostQueryArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('post_id',type=str)

post_list_fields={
        'id':fields.String,
        'author':UserField,
        'title':fields.String,
        'location':LocationField,
        'active_time':fields.DateTime,
        'category':fields.Integer,
        'followers':LengthField,
        'content':fields.String,
        }

post_fields={
        'id':fields.String,
        'author':UserField,
        'title':fields.String,
        'location':LocationField,
        'active_time':fields.DateTime,
        'category':fields.Integer,
        'followers':LengthField,
        'content':fields.String,
        'imageurl':KeyURLField(attribute='imagekey'),
        'waveurl':KeyURLField(attribute='wavekey'),
        }

class PostListResource(Resource):
    @authenticated()
    def post(self):
        """add an new item to Post collection"""
        args=PostListPostArgs().args
        return marshal(add_post(**args),post_list_fields)

    @authenticated()
    def get(self):
        """get items which could be seen by current user"""
        args=PostListQueryArgs().args
        return marshal(get_post_list(**args),post_list_fields)

class PostResource(Resource):
    @authenticated()
    def get(self,post_id):
        """get a post deatails"""
        #args=PostQueryArgs().args
        return marshal(get_post(post_id=post_id),post_fields)
