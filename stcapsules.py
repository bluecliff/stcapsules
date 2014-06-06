#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.restful import Api
from resources.user import UserResource
from resources.post import PostResource,PostListResource
from resources.comment import CommentResource

app = Flask(__name__)
api = Api(app)
api.add_resource(UserResource,'/api/login/')
api.add_resource(PostResource,'/api/post/<string:post_id>/')
api.add_resource(PostListResource,'/api/posts/')
api.add_resource(CommentResource,'/api/comments/<string:post_id>/')

app.secret_key='lijsf'

