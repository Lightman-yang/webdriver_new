#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/11/20 23:29
from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from zhiJieCaoZuo import *
driver=JieZheCaoZuo().comehome()
print('1')

time.sleep(2)
z=driver.window_handles
zzzzz=driver.switch_to_window(z[0])
print(len(z))
zz=driver.current_url
zzzz=driver.title
print(zz,zzzz)
ul=driver.find_elements_by_tag_name('ul') and driver.find_elements_by_xpath('/html/body/div[2]/div[2]/ul')
print(len(ul),'+121212')
list=ul[0].find_elements_by_tag_name('li') and ul[0].find_elements_by_id('coursePlayer')
print(len(list))
element1 = list[0]
driver.execute_script("arguments[0].click();", element1)

#zzz[2].find_element_by_class('iconfont icon-open-across').click()
# print(driver.execute_script("document.title='\u200e'"))
# driver.find_element_by_id('kw').send_keys("python")
# driver.find_element_by_id('su').click()
print("执行成功！")
#driver.switch_to()

#driver.find_element_by_class_name("chapter").click()
#driver.find_element_by_xpath('//*[@id="coursePlayer"]').click()
js="var q=document.documentElement.scrollTop=30"
js_done="var q=document.documentElement.scrollTop=0"
js_done_ten="var q=document.documentElement.scrollTop=60"
js_done_in='document.getElementsByClassName("scroll")[0].scrollTop=0'
js_done_in1='document.getElementsByClassName("scroll")[0].scrollTop=10000'
js001="var q=document.body.scrollTop=0"
js002 = "var q=document.body.scrollTop=100000"
js0001="q=document.getElementByClassName('player-right').scrollTop=100"
js00001="q=document.getElementByClassName('player-right').scrollTop=1000"
i=0
M=30000000
for i in range (1,M):
    print("第"+str(i)+"次！")
    time.sleep(2)
    # driver.execute_script(js)
    # time.sleep(20)
    # driver.execute_script(js_done)
    # time.sleep(20)
    # driver.execute_script(js_done_ten)
    list[0].execute_script(js0001)
    time.sleep(2)
    list[0].execute_script(js00001)
print(driver.title)

print("结束"+str(M)+"次滚动循环已经结束！ ")
