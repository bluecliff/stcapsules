#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.restful import Api
from resources.user import UserResource
from resources.post import PostResource,PostListResource
from resources.comment import CommentResource
from resources.favourite import FavouriteResource
from resources.receive import ReceiveResource

app = Flask(__name__)
api = Api(app)
api.add_resource(UserResource,'/api/login/')
api.add_resource(PostResource,'/api/post/<string:post_id>/')
api.add_resource(PostListResource,'/api/posts/')
api.add_resource(CommentResource,'/api/comments/<string:post_id>/')
api.add_resource(FavouriteResource,'/api/favs/')
api.add_resource(ReceiveResource,'/api/receives/')

app.secret_key='lijsf'

