#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.restful import Api
from resources.user import UserResource

app = Flask(__name__)
api = Api(app)
api.add_resource(UserResource,'/api/login/')

app.secret_key='lijsf'

