#!/usr/bin/env python
# encoding: utf-8

from storages.user_post_relation import User_Post_Relation
from storages.post import Post
from user import get_or_create
from config import DEFAULT_ITEMS
from utils import get_current_user

def get_favourite_items(**kwargs):
    """获取当前登录用户的收藏列表"""
    user =get_current_user()
    if user is None:
        return None
    try:
        upr=User_Post_Relation.objects().get(user=user)
        start=kwargs.pop('start',0)
        end=kwargs.pop('end',DEFAULT_ITEMS)
        return [post for post in upr.favourites[start:end]]
    except:
        return []

def add_favourite_item(post_id):
    """向当前用户增加一条收藏"""
    user=get_current_user()
    if user is None:
        return None
    try:
        upr=User_Post_Relation.objects().get(user=user)
        post=Post.objects.get(id=post_id)
        post.update(add_to_set__followers=user)#append(user)
        upr.update(add_to_set__favourites=post)
        return get_favourite_items()
    except:
        post=Post.objects.get(id=post_id)
        post.update(add_to_set__followers=user)#append(user)
        upr=User_Post_Relation(user=user,post=post).save()
        upr.update(add_to_set__favourites=post)
        return get_favourite_items()

def del_favourite_item(post_id):
    """从当前用户删除一条收藏"""
    user=get_current_user()
    if user is None:
        return None
    upr=User_Post_Relation.objects().get(user=user)
    post=Post.objects().get(id=post_id)
    post.update(pull__followers=user)
    upr.update(pull__favourites=post)
    return get_favourite_items()


def add_receives(post,receivers):
    """add a post to its receivers"""
    for user_id in receivers:
        user=get_or_create(user_id)
        try:
            upr=User_Post_Relation.objects().get(user=user)
            upr.update(add_to_set__receives=post)
            post.update(add_to_set__receivers=user)
        except:
            upr=User_Post_Relation()
            upr.user=user
            upr.receives.append(post)
            upr.save()
            post.update(add_to_set__receivers=user)
    """
    user=get_current_user()
    upr=User_Post_Relation.objects().get(user=user)
    return {'id':str(user.id),
            'user_id':user.user_id,
            'created_at':user.created_at,
            'favourites':len(upr.favourites),
            'receives':len(upr.receives)
            }
           """
def get_receives(**kwargs):
    """get the current user's receives list"""
    user=get_current_user()
    if user is None:
        return None
    start=kwargs.pop('start',0)
    end=kwargs.pop('end',DEFAULT_ITEMS)
    try:
        upr=User_Post_Relation.objects.get(user=user)
        return [post for post in upr.receives[start:end]]
    except:
        return []
