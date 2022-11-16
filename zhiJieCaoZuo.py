#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/4/7 18:21
from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from 登陆操作 import *
class JieZheCaoZuo(object):
      # Op = "新标签页 n"
   def comehome(self):
       chrome_options = webdriver.ChromeOptions()
       """快捷键属性里面设置chrome.exe后加入后面这段 --remote-debugging-port=7500 --user-data-dir="D:\chrom_webdriver\chromedriver_win32_96.0.4664.45" """
       chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:7500")

       chrome_driver = "D:\chrom_webdriver\chromedriver_win32_96.0.4664.45\chromedriver.exe"

       driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)

       return driver
'''
       rationew=fuzz.ratio(Op,driver.title)
       while int(rationew)>=80:
             print(type(driver))
             f=1
             if __name__ == '__main__':

               driver.implicitly_wait(5)
               login1().driverweb(driver)
               f=2
             break
       rationew='12'
'''
