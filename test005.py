#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/9/2 15:55
#from numpy import append


def JiaFa(self):
      n=[]
      # a = [4,16,18,19,27,28]  # 4
      for i in range(1, len(self)):
          zz = self[0] + self[i]
         # print(i, "次")
          n.append(zz)

          if int(zz) <= 33:
              #print(zz," ",end='')
              print(end='',)

          else:
              pass




      #print("第一个数加后面的数据" ,n)
      return n

def JianFa(self):
    n = []
    # a = [4,16,18,19,27,28]  # 4
    for i in range(2, len(self)+1):
        zz = self[len(self)-1]-self[len(self)-i]
        #print(a[len(a)-i])
        # print(i, "次")
        n.append(zz)

        if int(zz) >= 0:
             print(end='')


        else:
            pass
    #print("最后一个减去前面的数值", n)

    return n
def forxunh(self):
    for i in range(0,self):
        o=i
        return o
if __name__ == '__main__':
    import test007
    '''#zz的list集
      可以获得 len(zz)
    '''
    zz=list(test007.excelboot01())
    zzNi1=zz.reverse() #调用 list.reverse() 的返回值是 None ，它逆序的结果直接体现在原来的列表里面
    #z=zz[0:2]
    #zz=list(map(int,zz1))
    #print(z)
    '''
    a = [4,16,18,19,27,28]  # 4 今日
    b=[2,6,7,15,20,21]      #   昨天
    '''
    num001=[]
    num002=[]
    num003=[]
    num004=[]

    for i in range (0,len(zz)-1):
        #print(len(zz))
        #b=zz[i]

        b= list(map(int, zz[i]))#map将str的list转换为int的list
        #a=zz[i+1]
        a=list(map(int, zz[i+1]))#map将str的list转换为int的list
        #print(type(b),' ',a)

        zlist=JiaFa(b)
        zlist2=JianFa(b)
        zlist3=set(b) & set(a)
        z1=set(a)&set(zlist2)   # 最后一个减去前面的数值 [1, 6, 14, 15, 19]
        z2=set(a)&set(zlist)
        num001.append(z1)
        num002.append(z2)
        num003.append(a)
        num004.append(zlist3)
        print("中'%s'" % a)
        print("前面加'%s'" % z2)
        print("最后减去'%s'" % z1)
        print("重复'%s'" % zlist3)
        #print("中'%s'，最后的数减去前面的数下'%s'，前面的数加上后面的数据下'%s'" % (a,z1,z2))


        '''
    print("中'%s'" % num003)
    print("前面加'%s'" % num002)
    print("最后减去'%s'" % num001)
    print("重复'%s'" % num004)
    
'''
    zzNew=zz['Sheet2']
    for  i in range (1,len(num001)):

        zzNew.cell(row=i,column=2,value="%s" %num001[i])
    zzNew.save("test.xlsx")
    zzNew.close()