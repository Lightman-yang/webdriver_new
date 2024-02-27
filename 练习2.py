# bianliang = time.strftime("%Y年%m月%d日 %H点钟%M分%S秒", time.localtime())
# print(bianliang)
# a='1,19,355|1,737,412'
# num=2
# i=1
# for i in range(1,10):
#     if i == num:
#         print(1)
#
#     else:
#        print(2)
#        continue
# time.sleep(3)
# a=['1', '19', '355', '1', '737', '412']

# ss=a.strip('|')
# print(a)
# array=a.split('|')
# arrayN=[]
# for i in range(len(array)):
#   array1=array[i].split(',')
#   arrayN.append(array1)
# print(arrayN)
# for i in range(len(arrayN)):
#     if int(arrayN[i][1]) > 300:
#         print(arrayN[i])
#         print(int(arrayN[i][0]),type(int(arrayN[i][1])))
# a=(49,84,849,684)
# re=[]
# for i in range(2,len(a))[::3]:
#     print(i)
#     print(a[i])
#     if int(a[i-1])>300:
#
#         print(a[i-1], a[i])


# print(re)

# aa1= ["熟练者", "#422", "功师", 422]
# aa1, bb1, cc1, dd1 = "熟练者", "#422", "功师", "#422"
# def aad(aa1, bb1, dd1 ,cc1=0,ss1=0):
#     print(aa1, bb1, dd1 ,cc1,ss1)
# if __name__ == '__main__':
#     print(aad.__defaults__) #查找默认值用的 某某.__defaults__
#     print()
#     aa1 = ["熟练者", "#422", 422,]
#     aad(*aa1)
# class zz():
import time

a = []


def aaa():
    for i in range(1, 10):
        if i == 1:
            # print(1)
            a.append(i)
        else:
            # print(2)
            # print(i)
            a.append(i)

    return a



if __name__ == '__main__':
    aa = []
    mess="开""工"'大''典'
    print(mess)
    time.sleep(1000)









    print(aaa())
    print(type(aaa()))
    if 1 in aaa():
        print(1)
    else:
        print(0)
