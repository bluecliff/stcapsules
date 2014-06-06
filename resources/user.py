#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,reqparse,marshal_with
from flask import session
from models.user import get_user

parser=reqparse.RequestParser()
parser.add_argument('user_id',type=str)

user_fields={
#        'id':fields.String,
        'user_id':fields.String,
        'favourites':fields.Integer,
        'receives':fields.Integer,
        }

class UserResource(Resource):
    '''用user_id登录'''
    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        try:
            user=get_user(user_id=args['user_id'])
            session['user']=user['id']
            return user
        except:
            return None
