#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,reqparse,marshal_with
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
    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        try:
            user=get_user(args['user_id'])[0]
            session['user']=str(user.id)
            return user
        except:
            user=add_user(args['user_id'])
            session['user']=str(user.id)
            return user
