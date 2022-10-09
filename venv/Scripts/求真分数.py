#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/5/27 17:23
#list_1=input().split()
from fractions import Fraction
Height=input().split()
Height2=input().split()
s=[Height]
s2=[2 for dD in range(len(Height2))]
# print(s,s2)
# for i in range(len(s)):
#     for j in range(len(s2)):
#         FX=Fraction(int(i),int(j))
#         print(i,j)
a=12
b=22
fx=Fraction(a,b)
print(fx)