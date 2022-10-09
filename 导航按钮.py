#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/4/12 17:24
from datetime import time
from idlelib import window
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import ActionChains

from python_webdriver登陆 import *
from selenium.webdriver.chrome.options import Options
from zhiJieCaoZuo import *

from time import strftime, localtime
JieZheCaoZuo()  # 调用 接着执行操作.JieZheCaoZuo()
driver = JieZheCaoZuo.driver

if __name__ == '__main__':
    iframe1 = driver.find_elements_by_tag_name('iframe')
    driver.switch_to.frame(iframe1[1])
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="nameOrSname"]').send_keys('23')
#     driver.implicitly_wait(30)
#     iframe1 = driver.find_elements_by_tag_name('iframe')
#     for ss in iframe1:
#         driver.implicitly_wait(5)


# iframe = driver.switch_to_frame(iframe1)

    # driver.implicitly_wait(5)
    # driver.find_element_by_xpath('//*[@id="nameOrSname"]').send_keys('23')



    driver.refresh()  # 刷新方法 refresh

    # driver.implicitly_wait(62)
    # iframe=driver.find_element_by_id("d1961473281")
    # print(iframe)
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

    """在一些网页中经常会看到ifrmae/frame标签，iframe是嵌入式框架一般用来在已有的页面中嵌入另一个页面，当一个元素在iframe里时我们应该先切换到iframe里面。
    
    语法
    """
    driver.implicitly_wait(30)
    JieZheCaoZuo()  # 调用 接着执行操作.JieZheCaoZuo()
    driver = JieZheCaoZuo.driver
    driver.implicitly_wait(30)
    iframe1 = driver.find_elements_by_tag_name('iframe')
    driver.switch_to.frame(iframe1[0])
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="nameOrSname"]').send_keys('23')

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    print('执行过了')

    '''鼠标悬停'''
    driver.implicitly_wait(30)
    # driver.implicitly_wait(10)
    #定义鼠标悬停的元素：

    # move = driver.find_element_by_xpath('//*[@id="search"]')
    #模拟鼠标悬停：
    #
    # ActionChains(driver).move_to_element(move).click()
    driver.implicitly_wait(30)
    '''//*[@id="stdCode"]'''



    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    #driver.switch_to.frame(iframe)#'d1961473281'


    driver.switch_to.default_content()
    print(driver.title)

