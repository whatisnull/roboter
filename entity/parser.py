# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/28
"""

import re
import xmltodict


class Parser(object):

    def __init__(self, *args, **kwargs):
        pass

    def xml_to_dict(self, xml_str):
        return xmltodict.parse(xml_str)

