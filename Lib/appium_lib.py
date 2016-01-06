#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 10:14:36
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-18 15:25:10

from appium import webdriver
import time,sys
def login(driver,username,password):
    result = -1
    try:
        uname = driver.find_element_by_id('com.jlkj.janlinker:id/et_username')
        pword = driver.find_element_by_id('com.jlkj.janlinker:id/et_password')
        login_button = driver.find_element_by_id('com.jlkj.janlinker:id/login')
        uname.send_keys(username)
        pword.send_keys(password)
        login_button.click()
        result = 1
    except Exception as e:
        print 'login_error:',e
        result = 0
    finally:
        return result

def select_sn(driver,sn):
    result = -1
    try:
        snlist = driver.find_elements_by_id('com.jlkj.janlinker:id/tv_number')
        for i in snlist:
            print i.text.encode('utf-8').decode('utf-8')
            if i.text.encode('utf-8').split('(')[1] == sn +')':
                i.click()
                time.sleep(2)
                result = 1
                break
        
    except Exception as e:
        print 'select_sn_error:',e
        result = 0
    finally:
        return result

def login_to_page(driver,username,password,sn):
    login_result = login(driver,username,password)
    if login_result != 1:
        return 0
    time.sleep(8)
    cur_activity = ''
    try:
        cur_activity=driver.current_activity
    except Exception as e:
        print e
    if cur_activity=='.ui.MainActivity':
        try:
            driver.find_element_by_id('com.jlkj.janlinker:id/negativeButton').click()
        except:
            pass
        return login_result
    s_sn_result = select_sn(driver,sn)
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/negativeButton').click()
    except:
        pass
    return s_sn_result

#open_menu
#return_val:[status:1/-1,menu_content:type:list]
#menucontent[0]:主页
#menucontent[1]:视频监控
#menucontent[2]:告警信息
#menucontent[3]:日志管理
#menucontent[4]:系统设置
#menucontent[5]:系统服务
#menucontent[6]:关于本机
def open_menu(driver):
    result = -1
    try:
        menu = driver.find_element_by_id('com.jlkj.janlinker:id/iv_menu')
        menu.click()
        menu_content = driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')
        result = [1,menu_content]
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def get_version(driver):
    result = -1
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_menu').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[-1].click()
        gwver = driver.find_element_by_id('com.jlkj.janlinker:id/txtgetgwVersion').text.encode('utf-8')
        softver = driver.find_element_by_id('com.jlkj.janlinker:id/txtgetSoftVersion').text.encode('utf-8')
        gateway_ver = gwver.split(':')[-1]
        #software_ver = softver.split(':')[-1]
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = gateway_ver[-5:]
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def clear_device(driver):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_info = menu_result[1][5].click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/icondetail')[0].click()
        device_num = 0
        try:
            device_num = len(driver.find_elements_by_id('com.jlkj.janlinker:id/tv_mac'))
        except:
            pass
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        for device in range(device_num):
            driver.find_elements_by_id('com.jlkj.janlinker:id/icondetail')[0].click()
            driver.swipe(810,150,110,160,1000)
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            time.sleep(5)
            driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def add_area(driver,areas):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in areas:
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":32, "y":448})
            area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(area)
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result



def add_area_devices(driver,area,devices):
    result = -1
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_menu').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":32, "y":448})
        area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(area)
        driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        for i in range(len(devices)):
            driver.find_element_by_id('com.jlkj.janlinker:id/adddeivces').click()
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":870, "y":110})
            time.sleep(5)
            driver.find_element_by_id('com.jlkj.janlinker:id/ercode_scan_by_hand').click()
            area_mac = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(devices[i][0])
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            driver.find_element_by_id('com.jlkj.janlinker:id/btn_queding').click()
            area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(devices[i][1])
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            #device[i][2]:1 智能家电 2 智能灯光
            driver.find_element_by_id('android:id/button'+devices[i][2]).click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result


def add_devices(driver,devices):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        for i in range(len(devices)):
            driver.find_element_by_id('com.jlkj.janlinker:id/adddeivces').click()
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":870, "y":110})
            time.sleep(5)
            driver.find_element_by_id('com.jlkj.janlinker:id/ercode_scan_by_hand').click()
            area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(devices[i][0])
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            driver.find_element_by_id('com.jlkj.janlinker:id/btn_queding').click()
            area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(devices[i][1])
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            #device[i][2]:1 智能家电 2 智能灯光
            driver.find_element_by_id('android:id/button'+devices[i][2]).click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result


def del_area(driver,areas_num):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in range(areas_num):
            driver.swipe(810,150,110,160,1000)
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def clear_area(driver):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        area_num = 0
        try:
            areas_num = len(driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView'))
        except:
            pass
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in range(areas_num):
            driver.swipe(810,150,110,160,1000)
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()

        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def clear_env(driver):
    result = -1
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_menu').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        area_num = 0
        try:
            area_num = len(driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView'))
        except:
            pass
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in range(area_num):
            driver.swipe(810,150,110,160,1000)
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[5].click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/icondetail')[0].click()
        device_num = 0
        try:
            device_num = len(driver.find_elements_by_id('com.jlkj.janlinker:id/tv_mac'))
        except:
            pass
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        for device in range(device_num):
            driver.find_elements_by_id('com.jlkj.janlinker:id/icondetail')[0].click()
            driver.swipe(810,150,110,160,1000)
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            time.sleep(5)
            driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def get_all_opendevice_in_light(driver):
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[1].click()
    result = []
    try:
        c = driver.find_elements_by_android_uiautomator('new UiSelector().checked(true)')
    except:

        return [-1]
    for i in c:
        try:
            r='-1'
            txt = i.text.encode('utf-8')
            if txt == '①开':
                r = '1'
                result.append(r)
            elif txt == '②开':
                r = '2'
                result.append(r)
            elif txt == '③开':
                r = '3'
                result.append(r)
        except Exception as e :
            print e
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[0].click()
    return result

def get_all_device(driver,index):
    '''
    :param driver:
    :param index: 1、智能灯光 2、智能家电 3、智能安防
    :return:
    '''
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[int(index)].click()
    result = []
    try:
        c = driver.find_elements_by_id('com.jlkj.janlinker:id/textview')
    except:
        return [-1]
    for i in c:
        try:
            txt = i.text.encode('utf-8')
            result.append(txt)
        except:
            result = [-1]
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[0].click()
    return result


def get_all_device_in_light(driver):
    return get_all_device(driver,1)

def get_all_device_in_device(driver):
    return get_all_device(driver,2)

def get_all_device_in_save(driver):
    return get_all_device(driver,3)

def control_device_in_device(driver):
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[2].click()
    cb = driver.find_elements_by_class_name('android.widget.CheckBox')
    result = 1
    for i in cb:
        try:
            print i.text.encode('utf-8')
            i.click()
            result = result * 1
        except Exception as e :
            print e
            result = result * 0
            break
    return result

def wait_for_status_test(driver,expected,times=60,duration=5):
    ret = -1
    for i in range(times/duration):
        time.sleep(duration)
        result = get_all_opendevice_in_light(driver)
        if len(result)!=0 and result[0] == expected:
            ret = 1
            break
    return ret

