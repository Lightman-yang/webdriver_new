#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/2/20 15:05
while True:
   data1=input("请输入一个数据：")

   try:
       data1=eval(data1)
       if type(data1)==float or type(data1)==int :
           break
   except:
       if data1 != float or data1 !=int:
           print('请输入正确数据:第一个"%s"数据异常，' % data1)
           pass


while True:
   data2=input("请输入另一个数据：")
   try:
       data2 = eval(data2)
       if type(data2)==float or type(data2)==int :
            break
   except:
      if data2!=float or data2!=int:
           print('请输入正确数据,第二个"%s"数据异常，' % data2)
           pass
num=float(data1)*float(data2)+float(data1)
print("%s*%s=%s" %(data1,data2,num) ,"按y继续计划！")
