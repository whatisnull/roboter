# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/17
"""

import unittest

from appium import webdriver
from utils.enums import Model
from utils.apk import ApkInfo


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
    remote = "http://127.0.0.1:%s/wd/hub" % device.get("port")

    return webdriver.Remote(remote, desired_caps), apk_base


class Interface(unittest.TestCase):

    def __init__(self, methodName='runTest', device=None):
        super(Interface, self).__init__(methodName)
        self.device = device

    def setUp(self):
        if self.device.get('platformName') == Model.ANDROID:
            (self.driver, self.apk_base) = set_driver(self.device)

    @staticmethod
    def parametrize(obj, device=None):
        loader = unittest.TestLoader()
        funcs = loader.getTestCaseNames(obj)
        suite = unittest.TestSuite()
        for func in funcs:
            suite.addTest(obj(func, device))
        return suite

    def close(self):
        self.driver.quit()
