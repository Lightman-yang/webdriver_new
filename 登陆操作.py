#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/4/9 10:16
import time

from selenium import webdriver
from fuzzywuzzy import fuzz
from selenium.webdriver.chrome.options import Options
from zhiJieCaoZuo import *

class login1:

    def driverweb(self,aa):
        urlweb = ('http://www.baidu.com', 'http://portal.czsh.pcitc.com', 'details-button', "proceed-link", 'username',
                  'password', 'sub', '//*[@id="details-button"]')
        passw = ('zhaocy', 'zhaocy@123')
        self.driver=webdriver.Chrome(aa)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()#窗体最大化
        self.driver.implicitly_wait(5)
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.find_element_by_id(urlweb[4]).send_keys(passw[0])
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id(urlweb[5]).send_keys(passw[1])

        element1 = self.driver.find_element_by_id(urlweb[6])
        self.driver.execute_script("arguments[0].click();", element1)
        print(self.driver.title+' n+1')
        return self.driver



