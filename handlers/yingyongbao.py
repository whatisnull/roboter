# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/28
"""

from entity.parser import Parser


class YingYongbao(Parser):

    def __init__(self, *args, **kwargs):
        super(YingYongbao, self).__init__()


    def get_url(self, response):
        soup = self.get_soup(response)
