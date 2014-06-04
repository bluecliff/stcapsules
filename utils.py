#!/usr/bin/env python
# encoding: utf-8

from models.user import get_user
from flask import session,abort
import functools

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
