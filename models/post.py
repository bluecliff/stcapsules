#!/usr/bin/env python
# encoding: utf-8

from storages.post import Post
from utils import get_current_user
from config import DEFAULT_ITEMS
import datetime
from models.user_post_relation import add_receives

def get_favourite_items(**kwargs):
    user =get_current_user()
    if user is None:
        return None
    ret=[]
    start=kwargs.pop('start',0)
    end=kwargs.pop('end',DEFAULT_ITEMS)
    for post_id in user.favourites[start:end]:
        try:
            post=Post.get(id=post_id)
            ret.append(post)
        except:
            continue
    return ret

def add_favourite_item(post_id):
    user=get_current_user()
    if user is None:
        return None
    fav=user.favourites
    fav.append(post_id)
    user.update(set__favourites=fav)
    return get_favourite_items()

def del_favourite_item(post_id):
    user=get_current_user()
    if user is None:
        return None
    fav=user.favourites
    fav.remove(post_id)
    user.update(set__favourites=fav)
    return get_favourite_items()

def add_post(**kwargs):
    """add an item to Post"""
    user=get_current_user()
    if user is None:
        return None
    post=Post()
    post['location']=[kwargs.pop('longitude'),kwargs.pop('latitude')]
    post['active_time']=datetime.datetime.utcfromtimestamp(kwargs.pop('active_time'))
    receivers=kwargs.pop('receivers')
    for key in kwargs:
        post[key]=kwargs[key]
    post['author']=user
    post.save()
    add_receives(post.id,receivers)
    return post

