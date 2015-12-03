#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
__author__ = 'liaoben'

import sys
sys.path.append('../../')
sys.path.append('../Lib')
from config import Config
from Lib import Common
from Lib import appium_lib
from Lib import configrw
from Lib import loglib as log
from Lib import maillib

class TestBasicFunction(Config):

    def __init__(self):
        Config.__init__(self)
        self.init_case()
        print self.log_file
