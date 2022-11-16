#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/3/22 13:01
import time
import selenium
from selenium import webdriver
import unittest
# class sever():
#   def drverss(self):
#      self.driver=webdriver.Chrome()
#      self.driver=webdriver.Remote
#      self.driver = webdriver.ChromeOptions()
#      self.driver.add_experimental_option('useAutomationExtension', False)
#      self.driver.add_experimental_option('excludeSwitches', ['enable-automation'])
#      self.driver.add_experimental_option("detach", True)

#链式执行操作，构造函数不需要返回
class dl():
  def __init__(self):

      global driver#加入全局变量防止浏览器直接退出
      self.driver =webdriver.Chrome("D:\chrom_webdriver\chromedriver_win32_97.0.4692.20\chromedriver.exe")
      self.driver.get('http://portal.czsh.pcitc.com')
      self.driver.implicitly_wait(30)
      time.sleep(0.5)
# class loginmomo(dl):

  def ErrorTxt2(self,driver3):#单击继续
      self.driver.find_element_by_id(driver3).click()
      time.sleep(0.5)
      self.driver.implicitly_wait(30)
      return self

  def ErrorTxt3(self, driver4):  # 单击继续
      self.driver.find_element_by_id(driver4).click()
      time.sleep(0.5)
      self.driver.implicitly_wait(30)
      return self
  def load(self):
      # from test3 import sever
      self.driver.webdriver.ChromeOptions()
      self.driver.add_experimental_option("detach", True)
      self.driver.implicitly_wait(30)
      return self
      # 打开chrome浏览器
  def PassWord(self,A,B):
      self.driver.find_element_by_id(B).send_keys(A)
      self.driver.implicitly_wait(30)
      return self
      #特殊登陆
  def SpecialLogin(self,C):
      element1 = self.driver.find_element_by_id(C)
      self.driver.execute_script("arguments[0].click();", element1)
      return self

  def maxMize(self):
      self.driver.maximize_window()  # 窗体最大化
      self.driver.implicitly_wait(30)
      time.sleep(0.5)
      return self
# class loginmomo2(dl):
#   def ErrorTxt3(self,driver4):
#       self.driver.find_elements_by_id(driver4).click()
#       time.sleep(5)
  def PintLittle(self):
      self.driver.implicitly_wait(30)
      zz=self.driver.title
      time.sleep(0.5)
      return self,zz
  def ClassClick(self,A):
      self.driver.find_elment_by_class(A).click()


if __name__ == '__main__':
  try:
      # 1.username 名称元素ID
      # 2.password 密码元素ID
      # 3.sub      跳转元素ID
      # 4.roll-nav nav-left   全部导航元素Class
    urlweb = ('username','password','sub','roll-nav nav-left')
    passw = ('lipp298', 'Pcitc12#$')
    zz=dl()
    zz.ErrorTxt2('details-button')
    zz.ErrorTxt3('proceed-link')
    zz.PassWord(passw[0],"username")
    zz.PassWord(passw[1],'password')
    zz.SpecialLogin(urlweb[2])
    zz.maxMize()#
    print(zz.PintLittle()[1])
    zz.ClassClick(urlweb[3])
    time.sleep(0.5)
    zz.load()


  except Exception as e :
      print('打印错误')+e# loginmomo2().ErrorTxt3('proceed-link')




# def ErrorTxt(self):#单击继续
#
#       a=driver.find_element_by_id(self).click()
#       #driver.execute_script("arguments[0].click();", element1)
#       print(a)
#
#
# def PassWord(self, A):
#      driver.implicitly_wait(30)
#      driver.find_element_by_id(self).send_keys(A)
#
# def ErrorTxt1(self):  # 单击登陆继续 因为是隐藏的按钮，所有需要用execute_script
#           # driver.find_element_by_id(self).click()
#           element1 = driver.find_element_by_id(self)
#           driver.execute_script("arguments[0].click();", element1)
# if __name__ == '__main__':
# #//*[@id="details-button"]  details-button
#           urlweb = ('http://www.baidu.com', 'http://portal.czsh.pcitc.com', 'details-button', "proceed-link", 'username',
#           'password', 'sub')
#           passw = ('lipp298', 'pclipp298')
#
#           #driver.get(urlweb[1])
#           time.sleep(5)
#           ErrorTxt(urlweb[2])
#           ErrorTxt(urlweb[3])
#           PassWord(urlweb[4], passw[0])
#           PassWord(urlweb[5], passw[1])
#           # time.sleep(100)
#           ErrorTxt1(urlweb[6])
#           time.sleep(10)