#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/9/3 16:31
import os
import openpyxl
#加载本地数据
def excelboot01():
    zzzzz1=[]
    #data =openpyxl.load_workbook(wu)
    data =openpyxl.load_workbook(r"D:\TEST001\test.xlsx")
    #获取活动表
    zz1=data.active
    #获取表A1数据
    #z_max=zz1.max_row #获取最大行数
    #z_min=zz1.min_row #获取最小行数
    for i in range (int(zz1.min_row),int(zz1.max_row+1)):
        zz = zz1['A%s' % i]
        zzz = zz.value
        zz_list = list(zzz.split("，")) # 用','分割并转换list数据
        zzzzz=zz_list[0:6]
        #print(type(zz.value),type(zz_list),zz_list[0:6])
        #print(zz_list[0:6],'第一行%s' %i)
        zzzzz1.append(zzzzz)#添加到zzzzz1变量中
        #print(zz_list,"最大行为'%s',第一行数据为'%s'" %  (zz1.min_row,zz1.max_row))

    #zz.close
    #print(zzzzz)
    return zzzzz1
'''
if __name__ == '__main__':

    ss=list(excelboot01()[0:30])
    print(ss)

'''
