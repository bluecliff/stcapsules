#!/usr/bin/env python
# encoding: utf-8

from storages.user import User
from storages.user_post_relation import User_Post_Relation


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

def get_user(**kwargs):
    user=get_or_create(kwargs['user_id'])
    try:
        upr=User_Post_Relation.objects().get(user=user)
        return {'id':str(user.id),
                'user_id':user.user_id,
                'created_at':user.created_at,
                'favourites':len(upr.favourites),
                'receives':len(upr.receives)
                }
    except:
        return{
                'id':str(user.id),
                'user_id':user.user_id,
                'created_at':user.created_at,
                }

def check_user(**kwargs):
    return User.objects(**kwargs)
