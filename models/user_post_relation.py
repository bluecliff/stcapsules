#!/usr/bin/env python
# encoding: utf-8

from storages.user_post_relation import User_Post_Relation
from storages.user import User
from storages.post import Post
from user import get_or_create


def add_receives(post,receivers):
    """add a post to its receivers"""
    for user_id in receivers:
        user=get_or_create(user_id)
        try:
            upr=User_Post_Relation.get(user=user)
            upr.receives.append(post)
            return upr
        except:
            upr=User_Post_Relation()
            upr.user=user
            upr.receives.append(post)
            upr.save()
            return upr
