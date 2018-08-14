# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/18
"""

from utils import set_time
from utils import get_logger
from common.retry import Retry
import selenium.common.exceptions
from entity.variable import Variable
from selenium.webdriver.support.ui import WebDriverWait

log = get_logger("Actions")


def elements_by(operate, driver):
    elements = {
        Variable.find_element_by_id: lambda: driver.find_element_by_id(operate["element_info"]),
        Variable.find_elements_by_id: lambda: driver.find_elements_by_id(operate["element_info"]),
        Variable.find_element_by_xpath: lambda: driver.find_element_by_xpath(operate["element_info"]),
        Variable.find_element_by_name: lambda: driver.find_element_by_name(operate['name']),
        Variable.find_elements_by_name: lambda: driver.find_elements_by_name(operate['name'])[operate['index']],
        Variable.find_element_by_class_name: lambda: driver.find_element_by_class_name(operate['element_info']),
        Variable.find_elements_by_class_name: lambda: driver.find_elements_by_class_name(operate['element_info'])[operate['index']],
        Variable.find_elements_by_xpath: lambda: driver.find_elements_by_xpath(operate['element_info'])[operate['index']],
    }

    return elements[operate["find_type"]]()


def send_keys(operate, driver):
    elements_by(operate, driver).send_keys(operate["text"])


def operate_swipe_left(operate, driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for i in range(operate["screens"]+1):
        driver.swipe(width / 4 * 3, height / 2, width / 4, height / 2, 500)
        set_time(2)


def operate_swipe_right(operate, driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for i in range(operate["screens"]+1):
        driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)
        set_time(2)


def operate_swipe_up(operate, driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for i in range(operate["screens"]+1):
        driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
        set_time(2)


def operate_swipe_down(operate, driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for i in range(operate["screens"]+1):
        driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
        set_time(2)

def operate_swipe(operate, driver):
    (x1, y1, x2, y2) = operate
    driver.swipe(x1, y1, x2, y2, 500)


def operate_swipe_up_half(operate, driver):
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    for i in range(operate["screens"] + 1):
        driver.swipe(width / 2, height * 3 / 4 / 2, width / 2, height / 4 / 2, 500)
        set_time(2)



def operate_click(operate, driver):
    elements_by(operate, driver).click()


def operate_back(operate, driver):
    driver.press_keycode(4)


class Actions(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, operate_list, flag=False):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: elements_by(operate_list, self.driver))
            flag = True
        except selenium.common.exceptions.NoSuchElementException:
            log.error("no data, please, check....")
        except:
            log.error("unknow error, please, check....")

        return flag

    @Retry(max_retries=1, return_on_failure=-1)
    def operate_element(self, operate_list, flag=-2):
        if self.find_element(operate_list):
            elements = {
                Variable.CLICK: lambda: operate_click(operate_list, self.driver),
                Variable.SEND_KEYS: lambda: send_keys(operate_list, self.driver),
                Variable.SEND_CODE: lambda: set_time(2),

                Variable.UP: lambda: operate_swipe_up(operate_list, self.driver),
                Variable.DOWN: lambda: operate_swipe_down(operate_list, self.driver),
                Variable.LEFT: lambda: operate_swipe_left(operate_list, self.driver),
                Variable.RIGHT: lambda: operate_swipe_right(operate_list, self.driver),

                Variable.SWIPE_CLICK: lambda: operate_swipe(operate_list, self.driver),
                Variable.BACK_CODE: lambda: operate_back(operate_list, self.driver),

            }

            elements[operate_list["operate_type"]]()
            flag = 1

        return flag



