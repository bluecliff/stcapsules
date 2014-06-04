#!/usr/bin/env python
# encoding: utf-8

from flask.ext.script import Manager,Server
from stcapsules import app

manager=Manager(app)

manager.add_command("runserver",Server(use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=8000)
    )

if __name__=="__main__":
    manager.run()
