# -*- coding: utf-8 -*-

"""
 Created by Dr.wang on 2018/5/17 22:22
"""

import os
import requests
import threading
from utils import get_logger
from multiprocessing import Process
from utils import get_command_response

log = get_logger("BaseServer")


class BaseServer(object):
    stop_server_cmd = "taskkill /f /im  node.exe"
    status_url = "http://127.0.0.1:%s/wd/hub/status"

    def __init__(self, devices):
        self.devices = devices

    def start_server(self):
        for device in self.devices:
            log.info("load device: %s", device)
            server_cmd = device.get("server")
            if 'appium' not in server_cmd:
                log.warn("this device: %s, has error, please check server cmd.", device.get("devices"))
                continue
            log.info("this device: %s start appium server for port: %s", device.get("devices"), device.get("port"))
            t1 = RunServer(server_cmd)
            p = Process(target=t1.start())
            p.start()

    def stop_server(self):
        get_command_response(self.stop_server_cmd)

    def re_start_server(self):
        self.stop_server()
        self.start_server()

    def is_runnig(self):
        res = dict()
        for device in self.devices:
            log.info("load device: %s, get appium server status.", device)

            try:
                r = requests.get(self.status_url % device.get("port"), timeout=20)
                res.setdefault(device.get("devices"), r.status_code)
            except:
                res.setdefault(device.get("devices"), 500)

        return res


class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)
