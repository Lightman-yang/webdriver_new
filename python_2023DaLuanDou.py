import math
import os
import time

import pydirectinput  as dt

from python_findpicture import Caozuolei1

bianliang = ['x', 'h', 'o', 'time']
c = Caozuolei1()
c.Set_Dict(0, "测试2.txt")
for i in range(1,212):
    bianliang[0] = math.ceil(i / 2)  # 默认先执行一次（c.Find_Str()直接调用查询一次 ）成功开始匹配 进去一次 ，i-1才是执行的成功开始匹配 i是未 开始匹配
    # math.ceil 方法向上除发取整数，如1/2 =0.5 约上去为1
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
            time.sleep(0.5)
            bianliang[1] = z

            zz = c.Find_Ocr(
                x1=0,
                y1=0,
                x2=1200,
                y2=1200,
                color_format="#105",
                sim=0.9,
                linesign=" ",
                isbackcolor=0)
            bianliang[2] = zz
            bianliang[3] = time.strftime("%Y年%m月%d日 %H点钟%M分%S秒", time.localtime())
            print(
                "-----{}几次------- + -----{}次斗循环操作-----找到了什么“{}”-----{}".format(bianliang[0], bianliang[1], bianliang[2],
                                                                               bianliang[3]))
            if z > 9 and '开始匹配' in zz:
                break

            else:
                dt.press('c')
                for j in range(1, 12):
                    dt.press('x')  # ：模拟按键按下
                    # dt.press('left')
                for h in range(1, 10):
                    time.sleep(0.4)
                    dt.press('x')  # ：模拟按键按下
                    time.sleep(1)
                    dt.press('s')

    else:
        pass
os.system("shutdown -s -t 30")  # 30秒关闭电脑
