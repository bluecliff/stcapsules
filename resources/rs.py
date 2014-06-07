#!/usr/bin/env python
# encoding: utf-8

##qiniu resource  token

from flask.ext.restful import Resource,marshal,fields
from bson.objectid import ObjectId
from utils import authenticated
from config import QINIU_AK,QINIU_SK,QINIU_BUCKET_NAME
import qiniu.rs
import qiniu.conf

class Uptoken(object):
    """generate uptoken"""
    def __init__(self):
        qiniu.conf.ACCESS_KEY=QINIU_AK
        qiniu.conf.SECRET_KEY=QINIU_SK
        self.policy=qiniu.rs.PutPolicy(QINIU_BUCKET_NAME)
        self.uptoken=self.policy.token()

rs_fields={
        'uptoken':fields.String,
        }

class RsResource(Resource):
    @authenticated()
    def get(self):
        uptoken=Uptoken()
        return {'uptoken':uptoken.uptoken}
        #return marshal({'uptoken':uptoken.uptoken},rs_fields)

class KeyResource(Resource):
    @authenticated()
    def get(self):
        key=str(ObjectId())
        return {'key':key}
