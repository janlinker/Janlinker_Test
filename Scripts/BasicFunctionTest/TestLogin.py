#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
__author__ = 'liaoben'

import os
from . import TestBasicFunction
from . import Common
from . import configrw as conf
from . import log
from . import appium_lib as al
from selenium import webdriver
from time import sleep

class TestLogin(TestBasicFunction):

    def setUp(self):
        self.testcases = conf.readcfg(__file__)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        sleep(5)

    def tearDown(self):
        print 'test end...'
        try:
            self.driver.quit()
        except Exception as e:
            print 'tearDown:',e

    #TestCase Logic
    def caseLogic(self,*args):
        #arg check
        arg_check_status = Common.checkArgs(3,*args)
        if arg_check_status != 1:
            msg = 'Args number Error!!!'
            log.WritetoLog(self.log_file,msg)
            return 0
        username,password,sn = args
        #case logic
        login_result = al.login_to_page(self.driver,username,password,sn)
        log.WritetoLog(self.log_file,'Login_result:'+str(login_result))
        assert login_result == 1
        return 1

    #excute TestCase
    def testFunc1(self):
        for case in self.testcases:
            TcStatus=-1
            try:
                if not Common.judgeCaseLevel(case,self.test_level):
                    continue
                msg=Common.printCaseStart(case)
                log.WritetoLog(self.log_file,msg)
                TcStatus = self.caseLogic(*case[3:])
            except Exception as e:
                TcStatus = 0
                msg= 'Error occurred:'+str(e)
                log.WritetoLog(self.log_file,msg)
            finally:
                pass
                msg=Common.setTcStatus(case[0],TcStatus) #Set Result
                log.WritetoLog(self.log_file,msg)
                msg=Common.printCaseEnd(case)
                log.WritetoLog(self.log_file,msg)

if __name__ == '__main__':
    pass