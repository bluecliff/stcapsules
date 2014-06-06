#!/usr/bin/env python
# encoding: utf-8

from models.user import get_user
from flask import session,abort
import functools
import math

def get_current_user():
    try:
        return get_user(id=session['user'])[0]
    except:
        return None

def authenticated(*req):
    def actualDecorator(method):
        @functools.wraps(method)
        def wrapper(self,*args,**kwargs):
            user=get_current_user()
            if not user:
                abort(403)
            return method(self,*args,**kwargs)
        return wrapper
    return actualDecorator

class Distance(object):
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.EARTH_RADIUS=6378.137
        self.distance=self.__get_distance()
    def __rad(self,d):
        return d*math.pi/180.0

    def __get_distance(self):
        radlat1=self.__rad(self.p1[1])
        radlat2=self.__rad(self.p2[1])
        a=radlat1-radlat2
        b=self.__rad(self.p1[0])-self.__rad(self.p2[0])
        s=2*math.asih(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
        s=s*self.EARTH_RADIUS
        return s

