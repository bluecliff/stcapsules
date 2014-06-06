#!/usr/bin/env python
# encoding: utf-8

from storages.user import User

def get_user(**kwargs):
    return [obj for obj in User.objects(**kwargs)]

def add_user(user_id):
    user=User()
    user.user_id=user_id
    try:
        user.save()
        return user
    except:
        return None

def get_or_create(user_id):
    try:
        user=User.objects().get(user_id=user_id)
        return user
    except:
        return add_user(user_id)

