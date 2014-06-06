#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import Resource,fields,marshal
from base import BaseArgs,UserField
from utils import authenticated
from models.comment import add_comment,get_comments

class CommentQueryArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('start',type=int)
        self.parser.add_argument('end',type=int)

class CommentPostArgs(BaseArgs):
    def rules(self):
        self.parser.add_argument('content',type=str)

comment_fields={
        'author':UserField,
        'content':fields.String,
        'created_at':fields.DateTime,
        }

class CommentResource(Resource):
    @authenticated()
    def get(self,post_id):
        args=CommentQueryArgs().args
        args['post_id']=post_id
        return marshal(get_comments(**args),comment_fields)

    @authenticated()
    def post(self,post_id):
        args=CommentPostArgs().args
        args['post_id']=post_id
        return marshal(add_comment(**args),comment_fields)
