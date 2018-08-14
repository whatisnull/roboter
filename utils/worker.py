# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/18
"""

from entity.executer import Executer

class Worker(object):

    def __init__(self, *args, **kwargs):
        self.executer = Executer(*args, **kwargs)

    def execute(self, *args, **kwargs):
        self.executer.execute(*args, **kwargs)
