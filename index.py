#-*- coding:utf-8 -*-

from bae.core.wsgi import WSGIApplication
import stcapsules

application = WSGIApplication(stcapsules.app)
