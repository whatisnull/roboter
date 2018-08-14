# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/18
"""

from utils import get_yam
from utils import set_time
from utils import get_logger
from entity.parser import Parser
from utils.actions import Actions
from entity.variable import Variable

log = get_logger("Executer")

class Executer(object):

    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get("driver")
        self.device = kwargs.get("device")
        self.reset = kwargs.get("reset", None)
        self.parser = Parser()

        self.action = Actions(self.driver)

    def execute(self, *args, **kwargs):
        res = dict()
        tasks = get_yam(kwargs.get("f"))
        res.setdefault("total", len(tasks))
        for task in tasks:
            log.info("start for task: %s, for device: %s", task, self.device)

            if self.reset and task.get("reset", None):
                log.warn("this task not need run.")
                continue

            if task.get("operate_type") == Variable.CHECK:
                status = self.action.find_element(task)
                if status:
                    log.info("pass check this element, and run next action")
                    continue
                else:
                    log.info("no pass check this element, and run next job")
                    break

            if task.get('webview'):
                print self.driver.contexts
                self.driver.switch_to.context('WEBVIEW_com.tencent.tbs')
                all_handles = self.driver.window_handles
                for handle in all_handles:
                    self.driver.switch_to_window(handle)
                    print self.driver.page_source
                    print "*"*90

            self.action.operate_element(task)

            # load page source need sleeps
            need_sleeps = task.get("sleeps")
            log.info("this task: %s, need sleep for: %s", task, need_sleeps)
            if need_sleeps:
                set_time(need_sleeps)





