import os
import time

import pydirectinput  as dt

from python_findpicture import Caozuolei1

c = Caozuolei1()
c.Set_Dict(0, "测试2.txt")
for i in range(1, 140):
    print(i)
    if c.Find_Str(
            x1=0,
            y1=0,
            x2=1000,
            y2=1000,
            string='开始匹配',
            color_format="#105",
            sim=0.9,
            isbackcolor=0) == 0:
        dt.moveTo(500, 500)
        for z in range(1, 21):

            dt.press('c')
            for j in range(1, 10):

                dt.press('x')  # ：模拟按键按下
            #dt.press('left')
            for h in range(1, 8):
                time.sleep(0.5)
                dt.press('x')  # ：模拟按键按下
            time.sleep(1)
            dt.press('s')
            print('i==', z)
    else:
        pass
#os.system("shutdown -s -t 30")  # 30秒关闭电脑
