#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/5/27 15:27
'''
题目导弹拦截题
输入：389 207 155 300 299 170 158 65
输出结果：6
         2
'''
DaoDan=input()
Height=input().split()
dp_1=[1 for dD in range(len(Height))]
dp_2=[1 for dX in range(len(Height))]
for i in range(len(Height)):
      Height[i]=int(Height[i])
for i in range(1,len(Height)):
    for j in range(i):
        if (Height[j]>Height[i] and dp_1[i] < dp_1[j]+1):
            dp_1[i]=dp_1[j]+1
        if(Height[j]<Height[i] and dp_2[i]<dp_2[j]+1):
            dp_2[i]=dp_2[j]+1
print(max(dp_1))
#print(max(dp_2))