#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,reqparse,marshal_with
from flask import session
from models.user import get_user

parser=reqparse.RequestParser()
parser.add_argument('user_id',type=unicode)
parser.add_argument('user_name',type=unicode)
parser.add_argument('avatar_url',type=unicode)
parser.add_argument('snp',type=int)

user_fields={
#        'id':fields.String,
        'user_id':fields.String,
        'user_name':fields.String,
        'avatar_url':fields.String,
        'snp':fields.Integer,
        'favourites':fields.Integer,
        'receives':fields.Integer,
        }

class UserResource(Resource):
    '''用user_id登录'''
    @marshal_with(user_fields)
    def post(self):
        args=parser.parse_args()
        try:
#            user=get_user(user_id=args['user_id'])
            user=get_user(**args)
            session['user']=user['id']
            return user
        except:
            return None
