#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,reqparse,marshal
from flask import session
from models.user import get_user,add_user

parser=reqparse.RequestParser()
parser.add_argument('user_id',type=str)

user_fields={
        'id':fields.String,
        'user_id':fields.String,
        'favourites':fields.String,
        }

class UserResource(Resource):
    '''查询是否存在这个user，如不存在，即增加这个user'''
    def post(self):
        args=parser.parse_args()
        user=get_user(args['user_id'])
        if user:
            session['user']=user.id
            return marshal(user,user_fields)
        user=add_user(args['user_id'])
        return marshal(user,user_fields)
