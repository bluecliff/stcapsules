#!/usr/bin/env python
# encoding: utf-8

from storages.post import Post
from storages.comment import Comment
from utils import get_current_user
from config import DEFAULT_ITEMS

def get_comments(**kwargs):
    start=kwargs.pop('start',0)
    end=kwargs.pop('end',DEFAULT_ITEMS)
    post=Post.objects.get(id=kwargs['post_id'])
    comments=[obj for obj in Comment.objects(post=post)[start:end]]
    return comments

def add_comment(**kwargs):
    start=0
    end=DEFAULT_ITEMS
    post=Post.objects.get(id=kwargs['post_id'])
    user=get_current_user()
    comment=Comment(author=user,post=post,content=kwargs['content'])
    comment.save()
    comments=[obj for obj in Comment.objects(post=post)[start:end]]
    return comments
