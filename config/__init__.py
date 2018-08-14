# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/5/16
"""
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

DEVICES_PATH = os.path.join(ROOT, "devices.yaml")

execfile(os.path.join(ROOT, "config_local.py"))
