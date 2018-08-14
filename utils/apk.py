# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/18
"""

from entity.apk import ApkBase

class ApkInfo(object):

    def __init__(self, *args, **kwargs):
        self.apk_base = ApkBase(apk_path=kwargs.get('apk_path'))

    def get_apk_size(self):
        return self.apk_base.get_apk_size()

    def get_apk_version(self):
        return self.apk_base.get_apk_version()

    def get_apk_name(self):
        return self.apk_base.get_apk_name()

    def get_apk_pkg(self):
        return self.apk_base.get_apk_pkg()

    def get_apk_activity(self):
        return self.apk_base.get_apk_activity()
