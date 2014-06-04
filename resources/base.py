#!/usr/bin/env python
# encoding: utf-8

from flask.ext.restful import fields,reqparse

class LengthField(fields.Raw):
    def format(self,value):
        return len(value)

class LocationField(fields.Raw):
    def format(self,value):
        return {'longitude':value['coordinates']}

class UserField(fields.Raw):
    def format(self,value):
        return value.id

class BaseArgs(object):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.rules()
        self.args=self.parser.parse_args()
    def rules(self):
        raise NotImplementedError
