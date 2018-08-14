# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/21
"""

import os
import config
from utils import get_yam
from utils import get_logger
from appium import webdriver
from utils.enums import Model
from utils.apk import ApkInfo
from common.retry import Retry
from utils.worker import Worker



log = get_logger("Tasks")


@Retry(max_retries=1, return_on_failure=(None, None))
def set_driver(device):
    desired_caps = {}
    apk_base = ApkInfo(apk_path=device.get('apk_path'))
    desired_caps['platformName'] = device.get("platformName")
    desired_caps['platformVersion'] = device.get("platformVersion")
    desired_caps['deviceName'] = device.get("deviceName")
    desired_caps['appPackage'] = apk_base.get_apk_pkg().get("package")
    desired_caps['appActivity'] = apk_base.get_apk_activity().get("activity")
    desired_caps['udid'] = device.get("deviceName")
    desired_caps['app'] = device.get('apk_path')
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    desired_caps["newCommandTimeout"] = 7200
    desired_caps['chromeOptions'] = {'androidProcess': 'WEBVIEW_com.tencent.tbs'}

    if device.get("reset"):
        desired_caps['fastReset'] = "False"
        desired_caps['fullReset'] = "False"
        desired_caps['noReset'] = "True"

    remote = "http://127.0.0.1:%s/wd/hub" % device.get("port")
    log.info("set driver: %s, remote service: %s", desired_caps, remote)

    return webdriver.Remote(remote, desired_caps), apk_base

class Tasks(object):

    _name_ = "Tasks"

    driver = None
    apk_base = None

    jobs_path = "/../jobs.jobs.yaml"

    def __init__(self, device=None):
        super(Tasks, self).__init__()
        self.device = device

        self.set_up_driver()

    def set_up_driver(self):
        if self.device.get('platformName') == Model.ANDROID:
            (self.driver, self.apk_base) = set_driver(self.device)

    def _get_apk_pkg(self):
        return self.apk_base.get_apk_pkg().get("package")

    def _get_jobs(self, job_path):
        return get_yam(job_path)

    def _task_action(self, f):
        w = Worker(driver=self.driver,
                   device=self.device.get("deviceName"),
                   reset=self.device.get("reset", None)
                   )
        w.execute(f=f)

    def general_action(self):
        if not self.device or not self.driver:
            log.warn("please, check remote service for this device: %s", self.device.get("deviceName"))
            return

        abs_yaml_path = os.path.join(config.ROOT+"/../", self.device.get("yamls_path"))
        for f in os.listdir(abs_yaml_path):
            log.info("load: %s, to task list.", f)
            self._task_action(os.path.join(abs_yaml_path, f))


    def action(self):
        if not self.device or not self.driver:
            log.warn("please, check remote service for this device: %s", self.device.get("deviceName"))
            return

        jobs_path = os.path.join(config.ROOT + "/../", self.device.get("yamls_path") + "/jobs.yaml")
        job = self._get_jobs(jobs_path)
        for item in job.get("jobs"):
            job_path = os.path.join(config.ROOT + "/../", "%s/%s/%s" % (self.device.get("yamls_path"), job.get("job_path"), item))
            log.info("job: %s", job_path)
            self._task_action(job_path)

        # self.close()

    def close(self):
        self.driver.quit()
