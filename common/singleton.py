# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2017/8/11
"""


def Singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return _singleton
