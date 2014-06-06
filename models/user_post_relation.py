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
    upr=User_Post_Relation.objects().get(user=user)
    start=kwargs.pop('start',0)
    end=kwargs.pop('end',DEFAULT_ITEMS)
    return [post for post in upr.favourites[start:end]]

def add_favourite_item(post_id):
    """向当前用户增加一条收藏"""
    user=get_current_user()
    if user is None:
        return None
    upr=User_Post_Relation.objects().get(user=user)
    post=Post.objects().get(id=post_id)
    post.followere.append(user)
    upr.favourites.append(post)
    return get_favourite_items()

def del_favourite_item(post_id):
    """从当前用户删除一条收藏"""
    user=get_current_user()
    if user is None:
        return None
    upr=User_Post_Relation.objects().get(user=user)
    post=Post.objects().get(id=post_id)
    post.followers.remove(user)
    upr.favourites.remove(post)
    return get_favourite_items()


def add_receives(post,receivers):
    """add a post to its receivers"""
    for user_id in receivers:
        user=get_or_create(user_id)
        try:
            upr=User_Post_Relation.objects().get(user=user)
            upr.receives.append(post)
            post.receivers.append(user)
            return upr
        except:
            upr=User_Post_Relation()
            upr.user=user
            upr.receives.append(post)
            upr.save()
            post.receivers.append(user)
            return upr

