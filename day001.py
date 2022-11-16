#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/9/5 17:54

import openpyxl

import test005
#ZZ=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
a=[ 3,5,8,17,25,31]

zz=test005.JiaFa(a)
jj=test005.JianFa(a)
print('加',"=",zz)
print("减","=",jj)
print('原数据','=',a)