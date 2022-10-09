#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/4/12 17:24
import re
import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from python_webdriver登陆 import *
from zhiJieCaoZuo import *
from 登陆操作 import *
JieZheCaoZuo()
login()
driver.refresh()
driver.implicitly_wait(30)
"""操作一级导航，润滑油-测试"""
zz.Xpathtxt("//*[@id='menu_276']/a/span[2]")
driver.implicitly_wait(30)
# """操作二级导航，基础油配置"""
driver.implicitly_wait(30)
zz.Xpathtxt('//*[@id="menu_1850375341"]/p/a/span[2]')
driver.implicitly_wait(30)
# """操作三级导航，工厂模型"""
zz.Xpathtxt('//*[@id="menu_641276914"]/p/a/span[2]')
driver.implicitly_wait(30)
# """操作页面导航，企业维护"""
zz.Xpathtxt('//*[@id="menu_1961473281"]/p/a')
time.sleep(10)
iframe1 = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(iframe1[1])
print(iframe1)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="nameOrSname"]').send_keys('23')
driver.implicitly_wait(5)
driver.find_element_by_id("search").click()
