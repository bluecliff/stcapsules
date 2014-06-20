#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import fields,reqparse
from config import QINIU_DOMAIN

class LengthField(fields.Raw):
    def format(self,value):
        return len(value)

class LocationField(fields.Raw):
    def format(self,value):
        return value

class UserField(fields.Raw):
    def format(self,value):
        return {
                'user_id':value.user_id,
                'user_name':value.user_name,
                'avatar_url':value.avatar_url,
                'snp':value.snp,
                }

class KeyURLField(fields.Raw):
    def format(self,value):
        if value:
            return QINIU_DOMAIN+str(value)
        else:
            return None

class BaseArgs(object):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.rules()
        self.args=self.parser.parse_args()
    def rules(self):
        raise NotImplementedError
