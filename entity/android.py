# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/17
"""

from utils import get_command_response
from utils import get_commend_response_ext


class Android(object):

    base_info_dict = {
        "release": "ro.build.version.release=",
        "model": "ro.product.model=",
        "brand": "ro.product.brand=",
        "device": "ro.product.device=",
        "memory": "MemTotal:",
        "cpu": "processor",
        "windows": "Physical size:"
    }

    info_cmd = "adb -s %s shell cat /system/build.prop "
    mem_cmd = "adb -s %s shell cat /proc/meminfo"
    cpu_cmd = "adb -s %s shell cat /proc/cpuinfo"
    phys_cmd = "adb -s %s shell wm size"

    def __init__(self, *args, **kwargs):
        self.device = kwargs.get('device')

    def get_phone_info(self):
        res = dict()
        output = get_commend_response_ext(self.info_cmd % self.device)
        # output = get_command_response(self.info_cmd % self.device)
        for line in output.split():
            for base_key, base_vale in self.base_info_dict.items():
                if base_vale in str(line).strip():
                    res.setdefault(base_key, str(line).strip()[len(base_vale):])
        return res

    def get_memory_total(self):
        res = dict()
        output = get_command_response(self.mem_cmd % self.device)
        for line in output:
            for base_key, base_vale in self.base_info_dict.items():
                if base_vale in line.strip():
                    res.setdefault(base_key, line.strip()[len(base_vale):])
                    res.setdefault("memory_int", int(line.strip()[len(base_vale):].replace("kB", "").strip()))
        return res

    def get_cpu_kernels(self):
        res = dict()
        output = get_command_response(self.cpu_cmd % self.device)
        for line in output:
            for base_key, base_vale in self.base_info_dict.items():
                if base_vale in line.strip():
                    res.setdefault(base_key, 0)
                    res[base_key] += 1
        return res

    def get_device_physical(self):
        res = dict()
        output = get_command_response(self.phys_cmd % self.device)
        for line in output:
            for base_key, base_vale in self.base_info_dict.items():
                if base_vale in line.strip():
                    res.setdefault(base_key, line.strip()[len(base_vale):])
        return res
