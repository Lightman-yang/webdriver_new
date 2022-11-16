#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/9/18 14:51
import time
import selenium
from selenium import webdriver

driver=webdriver.Chrome("D:\chrom_webdriver\chromedriver_win32_93.0.4577.15\chromedriver.exe")
driver.get('http://portal.czsh.pcitc.com')
driver.implicitly_wait(30)
print(driver.title)