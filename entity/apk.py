# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/17
"""

import os
import platform
from utils import get_command_response
from utils import get_commend_response_ext

class ApkBase(object):

    base_info_dict = {
        "version": "versionName=",
        "name": "application-label:",
        "package": "name=",
        "activity": "launchable-activity: name=",
    }

    apk_version_cmd = "aapt dump badging %s | %s package"
    apk_name_cmd = "aapt dump badging %s | %s application-label: "
    apk_pkg_cmd = "aapt dump badging %s | %s package:"
    apk_activity_cmd = "aapt dump badging %s | %s launchable-activity:"

    find_cmd_str = "findstr" if "windows" in platform.system().lower() else "grep"

    def __init__(self, *args, **kwargs):
        self.apk_path = kwargs.get('apk_path')

    def get_apk_size(self):
        return dict(size=str(round(os.path.getsize(self.apk_path)/(1024*1000), 2)) + "MB")

    def get_apk_version(self):
        res = dict()
        output = get_command_response(self.apk_version_cmd % (self.apk_path, self.find_cmd_str))
        for line in output:
            for ss in line.strip().split():
                for base_key, base_vale in self.base_info_dict.items():
                    if base_vale in ss.strip():
                        res.setdefault(base_key, ss.strip()[len(base_vale):].replace("'", ""))
        return res

    def get_apk_name(self):
        res = dict()
        output = get_command_response(self.apk_name_cmd % (self.apk_path, self.find_cmd_str))
        for line in output:
            for ss in line.strip().split():
                for base_key, base_vale in self.base_info_dict.items():
                    if base_vale in ss.strip():
                        res.setdefault(base_key, ss.strip()[len(base_vale):].replace("'", ""))
        return res

    def get_apk_pkg(self):
        res = dict()
        output = get_command_response(self.apk_pkg_cmd % (self.apk_path, self.find_cmd_str))
        for line in output:
            for ss in line.strip().split():
                for base_key, base_vale in self.base_info_dict.items():
                    if base_vale in ss.strip():
                        res.setdefault(base_key, ss.strip()[len(base_vale):].replace("'", ""))
        return res

    def get_apk_activity(self):
        res = dict()
        output = get_commend_response_ext(self.apk_activity_cmd % (self.apk_path, self.find_cmd_str))
        if output:
            res.setdefault("activity", output.split()[1].decode()[6:-1])
        # for line in output:
        #     for ss in line.strip().split():
        #         if "name=" in ss:
        #             res.setdefault("activity", ss.strip()[len("name="):].replace("'", ""))
        return res



