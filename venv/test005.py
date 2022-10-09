#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/11/21 0:12
from selenium import webdriver
driver= webdriver.Chrome()
driver.get('http://xxxx.com/')

print(driver.title)
