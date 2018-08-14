# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/17
"""

from entity.android import Android


class Phone(object):

    def __init__(self, *args, **kwargs):
        self.phone = Android(device=kwargs.get("device"))

    def get_phone_info(self):
        return self.phone.get_phone_info()

    def get_memory_total(self):
        return self.phone.get_memory_total()

    def get_cpu_kernels(self):
        return self.phone.get_cpu_kernels()

    def get_device_physical(self):
        return self.phone.get_device_physical()

    def get_avg_raw(self):
        pass
