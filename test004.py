#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/9/2 11:21
while True:
    dada=input("请输入一个数值:_")
    try:
        dada=eval(dada)
        if type(dada) ==int :
           while True:
               dada1 = input("请输入满足一个数值:_")
               try:
                   dada1=eval(dada1)
                   if type(dada1) ==int :
                      i=1
                      for i in range (1,1000):
                           c=dada
                           a=dada*0.05
                           dada=a+dada
                           print(c,"+",a,"+","=",dada,"第%s次" % i)
                           if c>=dada1:
                                 break
                           else:
                                  pass
                   else:
                        pass
               except:
                      print('请输入正确数据:第一个"%s"数据异常，' % dada1,)
                      pass
    except:
           print('请输入正确数据:第一个"%s"数据异常，' % dada1)
           pass