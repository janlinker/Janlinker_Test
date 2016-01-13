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

class TestArea(TestBasicFunction):

    def setUp(self):
        self.testcases = conf.readcfg(__file__)


    def tearDown(self):
        print 'test end...'
        try:
            self.driver.quit()
        except Exception as e:
            print 'tearDown:',e

    #TestCase Logic
    def caseLogic(self,*args):
        try:
            #connect to device
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            sleep(5)
            #arg check
            arg_check_status = Common.checkArgs(3,*args)
            if arg_check_status != 1:
                msg = 'Args number Error!!!'
                log.WritetoLog(self.log_file,msg)
                return 0
            area_name,shuangkai_mac,shuangkai_name = args
            #case logic
            #Login
            login_result = al.login_to_page(self.driver,self.username,self.password,self.sn)
            log.WritetoLog(self.log_file,'Login_result:'+str(login_result))
            assert login_result == 1
            sleep(5)
            #Add area and device
            '''
            device_list = [[shuangkai_mac,shuangkai_name,'2']]
            add_device_result = al.add_area_devices(self.driver,area_name,device_list)
            assert add_device_result == 1
            '''
            #Check device
            device_list = al.get_all_device_in_light(self.driver)
            assert shuangkai_name in device_list
            self.result = 1
        except Exception as e:
            self.result = 0
            msg= 'Error occurred:env clear'
            log.WritetoLog(self.log_file,msg)
            try:
                self.driver.quit()
            except:
                pass
            driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            sleep(5)
            self.login_result = al.login_to_page(driver,self.username,self.password,self.sn)
        finally:
            #teardown
            try:
                if not 'driver' in dir():
                    driver = self.driver
                #self.env_clear_result  = al.clear_env(driver)
                #assert self.env_clear_result == 1
                log.WritetoLog(self.log_file,'环境恢复成功！')
            except Exception as e:
                print e
                log.WritetoLog(self.log_file,'环境恢复失败！')
            finally:
                try:
                    driver.quit()
                except:
                    pass
            return self.result

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