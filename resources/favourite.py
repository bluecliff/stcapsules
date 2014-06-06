#!/usr/bin/env python,add_favourite_item,del_favourite_item
# encoding: utf-8
from flask.ext.restful import Resource,fields,marshal
from models.user_post_relation import get_favourite_items,add_favourite_item,del_favourite_item
from base import BaseArgs,LocationField,UserField,LengthField
from utils import authenticated

class FavQueryArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('start',type=int)
        self.parser.add_argument('end',type=int)

class FavPostArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('post_id',type=str)

class FavDeleteArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('post_id',type=str)

fav_fields={
        'id':fields.String,
        'author':UserField,
        'title':fields.String,
        'location':LocationField,
        'active_time':fields.DateTime,
        'category':fields.Integer,
        'followers':LengthField,
        }

class FavouriteResource(Resource):
    @authenticated()
    def get(self):
        args=FavQueryArgs().args
        return marshal(get_favourite_items(**args),fav_fields)

    @authenticated()
    def post(self):
        args=FavPostArgs().args
        return marshal(add_favourite_item(args['post_id']),fav_fields)

    @authenticated()
    def delete(self):
        args=FavDeleteArgs().args
        return marshal(del_favourite_item(args['post_id']),fav_fields)

