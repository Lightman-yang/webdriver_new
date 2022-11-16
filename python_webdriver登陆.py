#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2020/12/18 16:49
import selenium
import time
from selenium import webdriver

from selenium import webdriver



class zzbb:


    def __init__(self,driver2):#进入平台
      self.driver =webdriver.Chrome('D:\chrom_webdriver\chromedriver_win32_93.0.4577.15\chromedriver.exe')
      self.driver.implicitly_wait(30)
      self.driver.maximize_window(2)#窗体最大化
      self.driver.get(driver2)
      global driver


      self.driver.implicitly_wait(30)
    def ErrorTxt(self,driver3):#单击继续

      self.driver.find_element_by_id(driver3).click()
      #driver.execute_script("arguments[0].click();", element1)
    def PassWord(self,A,B):
      self.driver.implicitly_wait(30)
      self.driver.find_element_by_id(B).send_keys(A)



    def ErrorTxt1(self,C):  # 单击登陆继续 因为是隐藏的按钮，所有需要用execute_script
      #driver.find_element_by_id(self).click()
      element1 = self.driver.find_element_by_id(C)
      self.driver.execute_script("arguments[0].click();", element1)
    def  Xpathtxt(self,C):
      element1 = self.driver.find_element_by_id(C)
      self.driver.execute_script("arguments[0].click();", element1)
      return self



if __name__ == '__main__':

    urlweb=('http://www.baidu.com','http://portal.czsh.pcitc.com','details-button',"proceed-link",'username','password','sub','//*[@id="details-button"]')
    passw=('lipp298','pclipp298')
    driver1='D:\chrom_webdriver\chromedriver_win32_93.0.4577.15\chromedriver.exe'
    driver2='http://portal.czsh.pcitc.com'
    driver=webdriver.Chrome(driver2)
    zzbb.login(driver,driver1,driver2)
    time.sleep(5)
"""
    zz.Xpathtxt(urlweb[7])
    zz.ErrorTxt(urlweb[3])
    zz.PassWord(urlweb[4],passw[0])
    zz.PassWord(urlweb[5],passw[1])
    #time.sleep(100)
    zz.(urlweb[6])
    time.sleep(10)
"""