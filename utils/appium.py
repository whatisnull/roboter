# -*- coding: utf-8 -*-

"""
 Created by Dr.wang on 2018/5/17 22:21
"""

from entity import server


class AppiumServer(object):

    def __init__(self, devices):
        self.server = server.BaseServer(devices)

    def start_server(self):
        self.server.start_server()

    def stop_server(self):
        self.server.stop_server()

    def is_runnig(self):
        return self.server.is_runnig()
