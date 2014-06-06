#!/usr/bin/env python
# encoding: utf-8

from storages.post import Post,DISTANCE,CATEGORY
from config import DEFAULT_ITEMS
from utils import get_current_user
import datetime
from models.user_post_relation import add_receives
from mongoengine import Q

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
    add_receives(post,receivers)
    return post

def get_post_list(**kwargs):
    """get post list"""
    user=get_current_user()
    if user is  None:
        return None
    current_point=[kwargs['longitude'],kwargs['latitude']]
    start=kwargs.pop('start',0)
    end=kwargs.pop('end',DEFAULT_ITEMS)

    q1=Q(active_time__lte=datetime.datetime.utcnow())

    q2=[]
    for index,value in enumerate(DISTANCE):
        q2.append(Q(distance=index) & Q(location__near=current_point,location__max_distance=value))

    q3=[]
    q3.append(Q(category=CATEGORY['PUBLIC']))
    q3.append(Q(category=CATEGORY['ADS']))
    q3.append(Q(category=CATEGORY['PRIVATE']) & Q(author=user))
    q3.append(Q(category=CATEGORY['PROTECTED']) & Q(receivers=user))

    return [obj for obj in Post.objects(q1 & (q2[0] | q2[1] | q2[2] | q2[3]) &(q3[0]|q3[1]|q3[2]|q3[3]))[start:end]]

def get_post(**kwargs):
    """get a post with post_id"""
    return Post.objects().get(id=kwargs['post_id'])
