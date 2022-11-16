# -*- coding: utf-8 -*-
#开发人员  :light
#开发时间  :2022/1/10 16:08
import requests
import json

import logging
class web_requests(object):
    def __init__(self):
        pass

    def Interface(self):
         print(self)
         url = "http://10.238.232.133:8069/service-app/planm/companyPlanRecReport/list?monthlyBaseOilLinkCode=1&companyId=-1&startPlanInterval=2022-03&planState=-1&now=0.5096482044865911&endPlanInterval=2022-03&pageIndex=0&pageSize=10&sortField=&sortOrder=&pageNumber=0&_=1647502927375&username=lipp298" # 测试的接口url
         headers = {"Content-Type": "application/x-www-form-urlencoded",
                    #"Date": "Mon, 10 Jan 2022 11:05:14 GMT",
                    "Access-Control-Allow-Credentials": "true",
                    "Access-Control-Allow-Headers": "authorization,Authorization,DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type",
                    "Access-Control-Allow-Max-Age": "3600",
                    "Transfer-Encoding": "chunked",
                    "Access-Control-Allow-Methods": "POST,GET,OPTIONS,PUT,DELETE,PATCH,HEAD",
                    "Accept": "text/plain, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep - alive",
                    "Host": "10.238.232.133:8069",
                    "Origin": "http://10.238.232.133:8080",
                    "Referer": "http://10.238.232.133:8080/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}#消息头
         #data1 = {"beginDate": "2018-01-01", "endDate": "2018-04-01"}  # 接口传送的参数
         #data = Interface_path  # 接口传送的参数
         #r = requests.get(url=url, json=data, headers=headers)  # 发送请求
         r = requests.get(url=url, headers=headers)  # 发送请求
         #return r.json
         print (r.text)  #获取响应报文
         print (r.status_code)
a = web_requests()
#a.Interface('monitor/sxsb-sxzl',beginDate="2018-01-01", endDate="2018-04-01")
#a.Interface('service-app/planm/baseOilAddPlanRelease/list',baseOilAddPlanLinkCode=1,companyId=38,startPlanInterval="2021-01",endPlanInterval=2022-12,planState=-1,now=0.5128893077814605,pageIndex=0,pageSize=10,sortField=,sortOrder=,pageNumber=0,_=1641808507374,username="lipp298")
#a.Interface("service-app/planm/baseOilAddPlanRelease/list?", baseOilAddPlanLinkCode=1, companyId=38, startPlanInterval='2021-01', endPlanInterval='2022-12', planState=-1, now=0.5128893077814605, pageIndex=0, pageSize=10, sortField=None, sortOrder=None, pageNumber=None, _='1641808507374', username="lipp298")
#a.Interface("service-app/planm/companyPlanRecReport/list?",monthlyBaseOilLinkCode=1,companyId=-1,startPlanInterval=2022-03,planState=-1,now=0.5096482044865911,endPlanInterval=2022-03,pageIndex=0,pageSize=10,sortField=,sortOrder=,pageNumber=0,_=1647502927375,username="lipp298)
a.Interface()
#a.Interface(monthlyBaseOilLinkCode=1,companyId='-1',startPlanInterval='2022-03',planState=-1,now=0.5096482044865911,endPlanInterval='2022-03',pageIndex=0,pageSize=10,sortField=0,sortOrder=0,pageNumber=0,username='lipp298')