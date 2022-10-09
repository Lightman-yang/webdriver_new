#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/1/13 17:21
import selenium
import time
from selenium import webdriver
import python_webdriver登陆

import random
import pymysql
#  ('10.238.232.153','root','root','lcpm')
db=pymysql.connect(host="10.238.232.153",user="root",password="root",db="lcpm",port=3306,use_unicode=True, charset="utf8")
cursor = db.cursor()
a=random.randint(200,500)
#t_om_bookinventory  as 账面库存信息
cursor.execute("INSERT INTO `lcpm`.`t_om_bookinventory`(`Book_Inventory_Id`, `Company_Id`, `Produce_Factory_Code`, `Material_Code`, `Material_Name`, `Finished_Product_Id`, `UnLimit_Stock`, `Quality_Stock`, `Blocked_Stock`, `Delivery_Num`, `Usable_Num`, `InTransit_Num`, `Book_Inventory`, `Measure_Unit`, `Net_Weight`, `Net_weight_Unit`, `Total_Weight`, `Crt_Time`, `Update_Time`) VALUES (2, 3, 'RYL6', '000609240060085133', '长城\\L-QB 300 导热油 散', 32, NULL, NULL, NULL, NULL, NULL, NULL, 200.00000, NULL, NULL, NULL, NULL, '2021-02-19 18:02:15', '2021-02-19 18:02:18');")
db.commit()#提交数据
db.close()