#!/usr/bin/env python
# encoding: utf-8

from storages.user import User

def get_user(user_id):
    return User.objects(user_id=user_id)

def add_user(user_id):
    user=User()
    user.user_id=user_id
    try:
        user.save()
    except:
        return None
    return user
