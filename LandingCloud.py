#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/9/28 class dl():
import time
from selenium import webdriver
class LandCloud():
  def __init__(self):

      global driver#加入全局变量防止浏览器直接退出
      self.driver =webdriver.Chrome("D:\chrom_webdriver\chromedriver_win32_93.0.4577.15\chromedriver.exe")
      self.driver.get('https://10.238.247.39/pages/login.do?isLogout=1')
      self.driver.implicitly_wait(30)
      time.sleep(0.5)
  def ErrorTxt2(self,driver3):#单击继续
      self.driver.find_element_by_id(driver3).click()
      time.sleep(0.5)
      self.driver.implicitly_wait(30)
      return self
  def maxMize(self):
      self.driver.maximize_window()  # 窗体最大化
      self.driver.implicitly_wait(30)
      time.sleep(0.5)
      return self
  def PassWord(self,A,B):
      self.driver.find_element_by_id(B).send_keys(A)
      self.driver.implicitly_wait(30)
      return self
  def alertWind(self):
      time.sleep(1)
      js = 'document.getElementById("doyoo_monitor").style.display="none";'
      self.driver.execute_script(js)
      return self
if __name__ == '__main__':
    urlweb=("userName","userPass","loginBtn")
    passw = ('t-chenyang.zhao', 'Zhao1234567')
    denglu=LandCloud()
    denglu.ErrorTxt2('details-button')
    denglu.ErrorTxt2('proceed-link')
    denglu.maxMize()
    denglu.PassWord(passw[0],urlweb[0])
    denglu.PassWord(passw[1],urlweb[1])
    denglu.ErrorTxt2(urlweb[2])
    denglu.alertWind()
    time.sleep(0.5)

    # encoding:utf-8

from selenium import webdriver
import time


