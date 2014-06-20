#!/usr/bin/env python
# encoding: utf-8

import mongoengine

DB_HOST='mongo.duapp.com'#'127.0.0.1'
DB_NAME='PuypNiLjvatfkUVZDJXB'#'stcapsules'
DB_PORT=8908
USER_NAME='Au2wGWafiyKBIDAMik4onX0d'
PASSWORD='7vaDG1eXI4TkqNTm4EEftkKzetXeudlO'

db=mongoengine.connect(DB_NAME,host=DB_HOST,port=DB_PORT,username=USER_NAME,password=PASSWORD)


'''
DB_HOST='127.0.0.1'
DB_NAME='stcapsules'
db=mongoengine.connect(DB_NAME,host=DB_HOST)
'''
