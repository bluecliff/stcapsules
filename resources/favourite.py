#!/usr/bin/env python,add_favourite_item,del_favourite_item
# encoding: utf-8
from flask.ext.restful import Resource,fields,marshal
from models.post import get_favourite_items,add_favourite_item,del_favourite_item
from base import BaseArgs,LocationField,UserField
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
        'title':fields.String,
        'author':UserField,
        'location':LocationField,
        'category':fields.Integer,
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

