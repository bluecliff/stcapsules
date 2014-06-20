#!/usr/bin/env python
# encoding: utf-8

from storages.user import User
from storages.user_post_relation import User_Post_Relation


def add_user(**kwargs):
    user=User()
    user.user_id=kwargs['user_id']
    user.user_name=kwargs['user_name']
    user.avatar_url=kwargs['avatar_url']
    user.snp=kwargs['snp']
    try:
        user.save()
        return user
    except:
        return None

def get_or_create(**kwargs):
    try:
        user=User.objects().get(user_id=kwargs['user_id'])
        return user
    except:
        return add_user(**kwargs)

def get_user(**kwargs):
    user=get_or_create(**kwargs)
    try:
        upr=User_Post_Relation.objects().get(user=user)
        return {'id':unicode(user.id),
                'user_id':user.user_id,
                'user_name':user.user_name,
                'avatar_url':user.avatar_url,
                'snp':user.snp,
                'created_at':user.created_at,
                'favourites':len(upr.favourites),
                'receives':len(upr.receives)
                }
    except:
        return{
                'id':unicode(user.id),
                'user_id':user.user_id,
                'created_at':user.created_at,
                'user_name':user.user_name,
                'avatar_url':user.avatar_url,
                'snp':user.snp,
                }

def check_user(**kwargs):
    return User.objects(**kwargs)
