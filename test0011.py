#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2022/9/5 18:14
import openpyxl

def xieRu(self,list2022):
        print(type(list2022))
        data1 = openpyxl.load_workbook(r"D:\TEST001\test.xlsx")
        data=data1[list2022]
        for i in range (int(len(self)),0,-1):

            print(len(self),type(i))
            data.cell(row=(1+i),column=2,value="%s" % self[i])
        data1.save("test.xlsx")
        data1.close()
if __name__ == '__main__':
    test=[[9, 10, 12, 18], [29, 32]]
    xieRu(test,'Sheet2')