# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/16
"""


import os
import re
import time
import yaml
import json
import logging
import hashlib
import subprocess


def get_logger(logger_name):
    logging.basicConfig(format="[%(asctime)s] %(filename)s: %(lineno)s: %(levelname)s: %(threadName)s: %(name)s: %(message)s", level=logging.INFO)
    return logging.getLogger(logger_name)


def get_command_response(cmd):
    return os.popen(cmd).readlines()

def get_commend_response_ext(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    (output, err) = p.communicate()
    return output

def obj_to_str(req):
    return json.dumps(req)

def str_to_obj(req):
    return json.loads(req)

def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)
    return None


def get_sign(url):
    md5 = hashlib.md5()
    md5.update(url)
    md5_digest = md5.hexdigest()
    return md5_digest


def get_current_time_milli():
    return int(time.time())


def get_current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def set_time(sleeps=1):
    time.sleep(sleeps)


def get_yam(yaml_path):
    try:
        with open(yaml_path) as f:
            return yaml.load(f)
    except:
        print(u'has unknow error')
