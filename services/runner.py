# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/16
"""

import os
import config
from utils import get_yam
from utils import set_time
from utils import get_logger
from utils.phone import Phone
from entity.tasks import Tasks
from multiprocessing import Pool
from utils.appium import AppiumServer

log = get_logger("runner")



def selector_devices(ds):
    res = []
    for d in ds.get("appium", []):
        if d.get("closed", False):
            log.info("this device is closed.")
            continue
        res.append(d)
    return res


def get_devices():
    ds = get_yam(config.DEVICES_PATH)
    return selector_devices(ds)


devices = get_devices()


def jobs_run(device_list):
    t = Tasks(device=device_list)
    t.action()


def servers_run():
    server = AppiumServer(devices)

    while True:
        server_status = server.is_runnig()
        for device, status in server_status.items():
            if status == 200:
                return True
            else:
                server.start_server()
                set_time(10)
            set_time(3)


def process_run():
    devices_Pool = []
    for device in devices:
        log.info("load device: %s", device)

        tmp = {}
        phone = Phone(device=device.get("devices"))
        tmp.setdefault("deviceName", device.get("devices"))
        tmp.setdefault("platformVersion", phone.get_phone_info().get("release"))
        tmp.setdefault("platformName", device.get("platformName"))
        tmp.setdefault("port", device.get("port"))
        tmp.setdefault("apk_path", os.path.join(config.ROOT+"/../", device.get("apk_path")))
        tmp.setdefault("yamls_path", device.get("yamls_path"))
        tmp.setdefault("reset", device.get("reset", None))

        devices_Pool.append(tmp)

    log.info("load total devices: %s", len(devices_Pool))

    pool = Pool(len(devices_Pool))

    pool.map(jobs_run, devices_Pool)
    pool.close()
    pool.join()


def run():
    log.info("devices: %s", devices)
    flag = servers_run()
    if flag:
        process_run()


if __name__ == '__main__':
    run()
