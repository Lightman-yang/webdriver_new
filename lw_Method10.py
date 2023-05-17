import os
import random
import time
from random import uniform
from time import sleep  # 导入时间休眠函数

import numpy as np
import pyautogui
import pydirectinput  as dt
from PIL import Image
from comtypes.client import CreateObject
from win32gui import FindWindow

from python_findpicture import Caozuolei1


# 继承Caozuolei1函数。
class Caozuolei(Caozuolei1):
    time.sleep(0.5)

    # # 绑定窗口句柄
    # # 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
    # # 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
    # dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发
    #
    # hwnd1 = win32gui.WindowFromPoint((308, 444))  # 请填写 x 和 y 坐标
    # print(hwnd1)
    # time.sleep(1)
    #
    # '''步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置'''
    # # 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
    # # left, top, right, bottom = win32gui.GetWindowRect('句柄值')
    # left, top, right, bottom = win32gui.GetWindowRect(hwnd1)
    # print(left, top, right, bottom)
    #
    # # 通过句柄将窗口放到最前
    # # win32gui.SetForegroundWindow("句柄值")
    # # dpyautogui.press('alt')
    # win32gui.SetForegroundWindow(hwnd1)
    # time.sleep(2)

    def __init__(self):
        super().__init__()
        # 当自身有构造方法时候，继承构造方法用super
        # 参数 窗口类名="地下城与勇士"
        self.hwnd = FindWindow("地下城与勇士", None)
        self.path = os.getcwd()
        try:
            self.lw = CreateObject('lw.lwsoft3')
        except OSError:
            print(self.path)
            os.system(r'regsvr32 /s %s\lw.dll' % self.path)
            self.lw = CreateObject('lw.lwsoft3')
        # 绑定窗口
        self.BindWindow()

    def BindWindow(self):
        self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        self.lw.BindWindow(self.hwnd, 0, 0, 0, 0, 0)
        # self.lw.EnableRealMouse(2,20,30)
        self.lw.SetDict(0, "find.txt")
        # print("find")

        # print("执行过了")

    # 获取窗口客户区域的宽度和高度,会设置X,Y。
    def GetClientSize(self):
        self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        ret = self.lw.GetClientSize(self.hwnd)
        self.width = ret[1]
        self.height = ret[2]

    # 解除绑定
    def UnBind(self):
        self.lw.UnBindWindow()
        print("解除绑定")
        # 按键key值是多少

    def KeyPress1(self, key):
        self.lw.KeyPress(key)

    # 按键操作，32代表space  1代表一次
    def KeyPress(self, num):
        for i in range(0, num):
            time.sleep(uniform(2.1, 4.9))
            s = self.lw.KeyPress(32, 1)
            print("跳", i + 1, "次")

    def MoveTo(self, x, y):
        self.lw.MoveTo(x, y)

    # 鼠标点击左键操作，理论是先进行鼠标移动，然后在进行鼠标点击左键操作
    def LeftClick(self, x, y, delay=uniform(0.01, 0.15)):
        self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        # def LeftClick(self, x1, y1, xr, yr, delay=uniform(0.3, 0.5)):
        #     self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        #     x = x1 + random.randint(0, xr)
        #     y = y1 + random.randint(0, yr)
        self.lw.MoveTo(x, y)
        self.lw.LeftClick()
        print("点击了鼠标左键")
        time.sleep(delay)

    def FindStrFastEx(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor, n=0):
        ret = self.lw.FindStrFastEx(x1, y1, x2, y2, string, color_format, sim, isbackcolor)

        if len(ret) > 0:
            ss = ret.split("|")
            print(ss)
            num = len(ss)
            s = ss[n].split(",")
            self.x = int(s[1])
            self.y = int(s[2])
            print(len(ret), self.x, self.y, "测试")
            return 1
        else:
            return 0

    def Find_Pic(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                 chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:

            print("找到图片, 横向坐标为：" + self.lw.x + "纵向坐标为：" + self.lw.y + "序号为：" + self.lw.idx)
        else:
            print("没有！")

    def movingFigur_Down(self, time_sleep):

        time.sleep(0.15)  # 按下两秒
        dt.keyDown('down')  # 向下移动
        time.sleep(time_sleep)  # 按下两秒
        dt.keyUp('down')  # ：模拟按键松开

    # 方法为像右移动
    def movingFigur_right(self, time_sleep):
        time.sleep(0.15)  # 像右移动
        dt.keyDown('right')  # 像右移动
        time.sleep(time_sleep)  # 像右移动
        dt.keyUp('right')  # ：模拟按键松开右

    # 方法为像上移动
    def movingFigur_up(self, time_sleep):
        time.sleep(0.15)  # 像右移动
        dt.keyDown('up')  # 像右移动
        time.sleep(time_sleep)  # 像右移动
        dt.keyUp('up')  # ：模拟按键松开右

    # 方法为像左移动
    def movingFigur_left(self, time_sleep):
        time.sleep(0.15)  # 像左移动
        dt.keyDown('left')  # 像左移动
        time.sleep(time_sleep)  # 像左移动
        dt.keyUp('left')  # ：模拟按键松开左

    def sleep_1000(self):
        while dt.press('+'):
            time.sleep(1000)
        else:
            dt.press('num9')

    def Coordinate_point(self, x, y):  # 坐标点
        # x11, y11 = left + 378, top + 452,
        x11, y11 = Caozuolei().left + x, Caozuolei().top + y,
        return x11, y11

    # 080037F840018002BFE37F8E06180C30192030406080C11F82000$行$0.0.66$15.14.15.14

    def movingfigur_Down(self, time_sleep):

        time.sleep(0.15)  # 按下两秒
        dt.keyDown('down')  # 向下移动
        time.sleep(time_sleep)  # 按下两秒
        dt.keyUp('down')  # ：模拟按键松开

    # 方法为像右移动
    def movingfigur_right(self, time_sleep):
        time.sleep(0.15)  # 像右移动
        dt.keyDown('right')  # 像右移动
        time.sleep(time_sleep)  # 像右移动
        dt.keyUp('right')  # ：模拟按键松开右

    # 方法为像上移动
    def movingfigur_up(self, time_sleep):
        time.sleep(0.15)  # 像右移动
        dt.keyDown('up')  # 像右移动
        time.sleep(time_sleep)  # 像右移动
        dt.keyUp('up')  # ：模拟按键松开右

    # 方法为像左移动
    def movingfigur_left(self, time_sleep):
        time.sleep(0.15)  # 像左移动
        dt.keyDown('left')  # 像左移动
        time.sleep(time_sleep)  # 像左移动
        dt.keyUp('left')  # ：模拟按键松开左

    # 字库
    def Set_Dict(self, index, file):

        ret = self.lw.SetDict(index, file)
        if ret == 1:
            print("自库设置成功！")

        else:
            print("自库设置失败！")

    def FuBen_INFO1(self):  # 副本地图信息数据实时获取
        time.sleep(0.4)
        c.Set_Dict(0, "测试2.txt")
        aa = c.Find_Ocr(
            x1=0,
            y1=0,
            x2=1200,
            y2=1200,
            color_format="#360",
            sim=0.85,
            linesign=" ",
            isbackcolor=0)
        print("打印aa", aa)
        if "靓仔" in aa:
            print(aa)
            time.sleep(30)  # 按下两秒
            dt.press('9')
            time.sleep(1)  # 按下两秒
        else:
            return

    def FuBen_INFO2(self):  # 副本地图信息数据实时获取
        c.Set_Dict(0, "测试2.txt")
        while True:
            time.sleep(1)
            aa = c.Find_Ocr(
                x1=0,
                y1=0,
                x2=1200,
                y2=1200,
                color_format="#360",
                sim=0.85,
                linesign=" ",
                isbackcolor=0)
            if "再次挑战" not in aa:
                dt.press('g')
                time.sleep(0.65)
                dt.press('y')
                time.sleep(0.75)  # 按下两秒
                dt.press('d')
                time.sleep(0.75)  # 按下19秒
                dt.press('f')


            else:
                return

    def FuBen_INFO3(self):  # 副本地图信息如果自动存在，证明没活力点了，直接退出
        c.Set_Dict(0, "测试2.txt")
        while True:
            time.sleep(1)
            aa = c.Find_Ocr(
                x1=0,
                y1=0,
                x2=1200,
                y2=1200,
                color_format="#360",
                sim=0.85,
                linesign=" ",
                isbackcolor=0)
            if "再次挑战" in aa:
                dt.press('f12')
                time.sleep(1)
                return 1


            else:
                return 0

    def FuBen_INFO(self):  # 副本地图信息数据实时获取

        while True:
            time.sleep(1)
            aa = c.Find_Ocr(
                x1=0,
                y1=0,
                x2=1200,
                y2=1200,
                color_format="#360",
                sim=0.85,
                linesign=" ",
                isbackcolor=0)
            if "五陵" in aa:
                print("在副本外面")
                continue

            elif "第一关" in aa and "开门" not in aa:
                print('第一关')
                continue
            elif "开门" in aa or ("第一关" in aa and "开门" in aa):
                print('第二关')
                continue
            elif "凹凸" in aa and "星星" not in aa:
                print("在第三关凹凸")
                continue
            elif "大鱼海棠" in aa or "夜空下" in aa:
                print("在第四关")
                continue
            elif "星星" in aa:
                print("在第5关")
                continue
            elif "花花" in aa and "好绿" not in aa:
                print("在6关")
                continue
            elif "好绿" in aa or (("好绿" in aa) and ("花花" in aa)):
                print("在7关")
                continue
            elif "最后" in aa and "再次挑战" not in aa:
                print("在boss房间")
                continue
            elif "再次挑战" in aa:
                print("通关完成")
                continue
            else:
                print("没找到")
                continue

    def nvQiGong(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter):
        # 女气功 花花

        for i in range(1, 60):
            time.sleep(0.5)
            num = num_parameter  # num不能是奇数 运行几次
            # move_seep = -0.52  # 57.7   气功4.2  40.8
            # move_seep1= -0.26

            move_seep = -move_seepx
            move_seep1 = -move_seepy
            # move_seep = -0.8  # 57.70
            # move_seep1 = -0.23
            m_button = 'h'
            print(move_seep)
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                if j == 1:
                    time.sleep(0.65)  # 按下两秒
                    dt.press('g')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(1.35)
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.5)
                    if Caozuolei().FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:

                        time.sleep(1)  # 按下两秒

                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键

                        time.sleep(1)  # 按下两秒
                        dt.keyDown('right')  # ：模拟按键按下 向下
                        time.sleep(1.5 + move_seep1)
                        dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 2:
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.65)
                    dt.press('g')
                    time.sleep(0.75)
                    dt.press('v')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    print('二操作9成功')
                    # time.sleep(1.2)
                    # Caozuolei().FuBen_INFO1()
                    time.sleep(2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.84 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 3:

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.66 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.5)  # 按下两
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('g')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')
                    time.sleep(0.5)  # 按下两秒
                    time.sleep(1.6)
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()

                    time.sleep(2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('f')
                    time.sleep(0.7)
                    dt.press('g')

                    time.sleep(2)
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    time.sleep(1.2)
                    time.sleep(1)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.9 + move_seep)
                    dt.keyUp('down')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.2 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.55 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按
                    dt.press('t')
                    time.sleep(1.5)
                    dt.press('t')
                    time.sleep(1.35)
                    dt.press('d')
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(2)
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.8 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('g')
                    time.sleep(1)

                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    # Caozuolei().FuBen_INFO1()
                    time.sleep(2)

                    time.sleep(1.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数

                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.9 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.8 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(1)
                    time.sleep(0.7)  # 按下19秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('d')

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.5 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒

                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 8:  # 奇数 反之偶数

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(0.65)  # 按下19秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下19秒
                    dt.press('f')
                    time.sleep(2)  # 按下两秒
                    Caozuolei().FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            from python_findpicture import Caozuolei1
                            Caozuolei1().sellGoods_xy()  # 点击一键出售按钮
                            print('等待')
                            time.sleep(1.5)  # 按下两秒
                            dt.press('a')
                            time.sleep(1)  # 按下两秒
                            dt.press('space')
                            time.sleep(1)
                            dt.press('left')
                            time.sleep(1)
                            dt.press('space')
                            break
                        else:
                            break
                    time.sleep(5)  # 按下两秒
                    dt.press('esc')

                    # print('0')
                    # print(i)

                    time.sleep(2)

                    if i == num:
                        dt.press('f12')
                    else:
                        dt.press('f10')
                    time.sleep(3)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 6
            if i == num and Restart_computer == 0:
                # os.system("shutdown -s -t 30")
                b = time.strftime("%y-%m-%d_%H$%M$%S", time.localtime())

                img = pyautogui.screenshot(region=[48, 84, 848, 684])
                img = Image.fromarray(np.uint8(img))
                img.save('D:\webdriver_new\lw\Tpshot{}s.png'.format(b))
                time.sleep(1)
                print(b)
                break
            elif i == num and Restart_computer == 1:
                os.system("shutdown -s -t 30")  # 30秒关闭电脑
                break

            print('费了{}疲劳'.format(sss))
        '''t
        dt.keyDown('a')#：模拟按键按下
        time.sleep(2) #按下两秒0
        dt.keyUp('a') #：模拟按键松开time.sleep(2)
        '''

    def kuangzhanshi(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter):
        # def nvQiGong(self, num_parameter, Restart_computer_parameter):
        # 女气功 花花

        for i in range(1, 60):
            time.sleep(2)
            num = num_parameter  # num不能是奇数 运行几次
            # move_seep = -0.52  # 57.7   气功4.2  40.8
            # move_seep1 = -0.26

            # move_seep = 0.189  # 57.70
            # move_seep1 = -0.23
            move_seep = move_seepx
            move_seep1 = -move_seepy
            m_button = 'h'
            print(move_seep)
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                if j == 1:
                    time.sleep(0.3)  # 按下两秒
                    dt.press('h')
                    time.sleep(0.54)  # 按下两秒
                    dt.press('g')
                    time.sleep(0.54)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.5)
                    if Caozuolei().FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:

                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键

                        time.sleep(1)  # 按下两秒
                        dt.keyDown('right')  # ：模拟按键按下 向下
                        time.sleep(1.5 + move_seep1)
                        dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 2:

                    time.sleep(1.2)
                    dt.press('t')
                    time.sleep(0.5)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    time.sleep(0.1)
                    dt.press('g')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    time.sleep(2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.84 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 3:

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.66 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')

                    time.sleep(2)
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('t')
                    time.sleep(0.7)
                    dt.press('g')

                    time.sleep(1.5)
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.9 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.2 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.3 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(1)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.8 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('g')
                    time.sleep(1)
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒

                    time.sleep(1.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数

                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.9 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.88)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒

                    time.sleep(1.5)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.45 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 8:  # 奇数 反之偶数

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.6 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('t')
                    time.sleep(0.55)  # 按下19秒
                    dt.press('f')
                    time.sleep(0.55)  # 按下19秒
                    dt.press('g')
                    time.sleep(2)  # 按下两秒
                    Caozuolei().FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            from python_findpicture import Caozuolei1
                            Caozuolei1().sellGoods_xy()  # 点击一键出售按钮
                            print('等待')
                            time.sleep(1.5)  # 按下两秒
                            dt.press('a')
                            time.sleep(1)  # 按下两秒
                            dt.press('space')
                            time.sleep(1)
                            dt.press('left')
                            time.sleep(1)
                            dt.press('space')
                            break
                        else:
                            break
                    time.sleep(5)  # 按下两秒
                    dt.press('esc')

                    # print('0')
                    # print(i)

                    time.sleep(2)

                    if i == num:
                        dt.press('f12')
                    else:
                        dt.press('f10')

                    time.sleep(3)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 6
            if i == num and Restart_computer == 0:
                # os.system("shutdown -s -t 30")
                b = time.strftime("%y-%m-%d_%H$%M$%S", time.localtime())

                img = pyautogui.screenshot(region=[48, 84, 848, 684])
                img = Image.fromarray(np.uint8(img))
                img.save('D:\webdriver_new\lw\Tpshot{}s.png'.format(b))
                time.sleep(1)
                print(b)
                break
            elif i == num and Restart_computer == 1:
                os.system("shutdown -s -t 30")  # 30秒关闭电脑
                break

            print('费了{}疲劳'.format(sss))
        '''t
        dt.keyDown('a')#：模拟按键按下
        time.sleep(2) #按下两秒0
        dt.keyUp('a') #：模拟按键松开time.sleep(2)
        '''

    def nanQiGong(self, num_parameter, Restart_computer_parameter):
        # 男气功

        for i in range(1, 60):
            time.sleep(2)
            num = num_parameter  # num不能是奇数 运行几次
            move_seep = -0.289  # 57.7
            m_button = 'h'
            print(move_seep)
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                if j == 1:
                    dt.press('h')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.85 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.45)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    time.sleep(0.85)
                    dt.press('9')
                    time.sleep(1)
                    if Caozuolei().FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:
                        time.sleep(0.5)  # 按下两秒
                        dt.keyDown('right')  # ：模拟按键按下 向下
                        time.sleep(1.5)
                        dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 2:

                    time.sleep(1)
                    dt.press('y')
                    time.sleep(1.78)  # 按下两秒
                    dt.press('y')
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(0.75)
                    Caozuolei().FuBen_INFO1()
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒

                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.84 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 3:
                    time.sleep(0.65)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.56)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(0.75)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.85 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.0075)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.985 + move_seep)

                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 5:
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.34 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.35)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    dt.press('t')
                    time.sleep(1.5)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.85 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.75)
                    dt.keyDown('right')
                    time.sleep(0.48)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.45)
                    dt.keyUp('right')  # ：模拟按键松开按
                    time.sleep(0.85)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.0075)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()

                    time.sleep(1.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数

                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.8 + move_seep)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.2)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.8)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')

                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 8:  # 奇数 反之偶数

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('right')  # ：模拟按键按下
                    for o in range(1, 6):
                        time.sleep(0.0155)  # 按下19秒
                        dt.press('x')

                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('left')
                    time.sleep(0.65)  # 按下19秒
                    dt.press('y')
                    time.sleep(0.65)  # 按下19秒
                    dt.press('f')
                    dt.press('e')
                    time.sleep(0.0075)  # 按下两秒
                    dt.press('e')
                    time.sleep(2)  # 按下两秒
                    Caozuolei().FuBen_INFO2()

                    dt.press('0')
                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            from python_findpicture import Caozuolei1
                            Caozuolei1().sellGoods_xy()  # 点击一键出售按钮
                            print('等待')
                            time.sleep(1.5)  # 按下两秒
                            dt.press('a')
                            time.sleep(1)  # 按下两秒
                            dt.press('space')
                            time.sleep(1)
                            dt.press('left')
                            time.sleep(1)
                            dt.press('space')
                            break
                        else:
                            break
                    time.sleep(5)  # 按下两秒
                    dt.press('esc')

                    # print('0')
                    # print(i)

                    time.sleep(2)

                    if i == num:
                        dt.press('f12')
                    else:
                        dt.press('f10')
                    time.sleep(3)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 6
            if i == num and Restart_computer == 0:
                # os.system("shutdown -s -t 30")
                b = time.strftime("%y-%m-%d_%H$%M$%S", time.localtime())

                img = pyautogui.screenshot(region=[48, 84, 848, 684])
                img = Image.fromarray(np.uint8(img))
                img.save('D:\webdriver_new\lw\Tpshot{}s.png'.format(b))
                time.sleep(1)
                print(b)
                break
            elif i == num and Restart_computer == 1:
                os.system("shutdown -s -t 30")  # 30秒关闭电脑
                break

            print('费了{}疲劳'.format(sss))
        '''t
        dt.keyDown('a')#：模拟按键按下
        time.sleep(2) #按下两秒0
        dt.keyUp('a') #：模拟按键松开time.sleep(2)
        '''

    def zhaohuan(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter):
        # 召唤

        for i in range(1, 60):
            time.sleep(0.5)
            num = num_parameter  # num不能是奇数 运行几次
            # move_seep = -0.52  # 57.7   气功4.2  40.8
            # move_seep1= -0.26

            move_seep = -move_seepx
            move_seep1 = -move_seepy
            # move_seep = -0.8  # 57.70
            # move_seep1 = -0.23
            m_button = 'h'
            print(move_seep)
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                if j == 1:
                    time.sleep(0.5)  # 按下两秒
                    dt.press('t')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('s')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.5 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    if Caozuolei().FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:
                        time.sleep(1)  # 按下两秒
                        dt.keyDown('right')  # ：模拟按键按下 向下
                        time.sleep(1.5 + move_seep1)
                        dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 2:

                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    dt.press('s')
                    time.sleep(3)
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.84 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 3:

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.66 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('s')
                    time.sleep(3)  # 按下两秒
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('s')
                    time.sleep(3)

                    time.sleep(1)
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(1)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.15)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.2 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.keyDown('up')  # ：模拟按键按下 向下gygygygy
                    time.sleep(1.68 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.05 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.8 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('s')
                    time.sleep(1)
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()
                    time.sleep(2)

                    time.sleep(1.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数

                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.9 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.8 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('s')
                    time.sleep(1)
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    Caozuolei().FuBen_INFO1()

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.5 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.5)
                    dt.press('9')
                    time.sleep(1.2)

                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 8:  # 奇数 反之偶数

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.5 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(0.45)  # 按下19秒
                    dt.press('s')
                    time.sleep(2)  # 按下两秒
                    Caozuolei().FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            from python_findpicture import Caozuolei1
                            Caozuolei1().sellGoods_xy()  # 点击一键出售按钮
                            print('等待')
                            time.sleep(1.5)  # 按下两秒
                            dt.press('a')
                            time.sleep(1)  # 按下两秒
                            dt.press('space')
                            time.sleep(1)
                            dt.press('left')
                            time.sleep(1)
                            dt.press('space')
                            break
                        else:
                            break
                    time.sleep(5)  # 按下两秒
                    dt.press('esc')

                    # print('0')
                    # print(i)

                    time.sleep(2)

                    if i == num:
                        dt.press('f12')
                    else:
                        dt.press('f10')
                    time.sleep(3)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 6
            if i == num and Restart_computer == 0:
                # os.system("shutdown -s -t 30")
                b = time.strftime("%y-%m-%d_%H$%M$%S", time.localtime())

                img = pyautogui.screenshot(region=[48, 84, 848, 684])
                img = Image.fromarray(np.uint8(img))
                img.save('D:\webdriver_new\lw\Tpshot{}s.png'.format(b))
                time.sleep(1)
                print(b)
                break
            elif i == num and Restart_computer == 1:
                os.system("shutdown -s -t 30")  # 30秒关闭电脑
                break

            print('费了{}疲劳'.format(sss))
        '''t
        dt.keyDown('a')#：模拟按键按下
        time.sleep(2) #按下两秒0
        dt.keyUp('a') #：模拟按键松开time.sleep(2)
        '''

    def FindStr(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor):
        ret = self.lw.FindStr(x1, y1, x2, y2, string, color_format, sim, isbackcolor)
        if ret == 1:
            return self.lw.x(), self.lw.y()
        else:
            return 0



if __name__ == '__main__':
    # move_seep = -0.54  # 57.7   气功4.2  40.8
    # move_seep1 = -0.26
    # 睡眠不足十62.5%
    time.sleep(1.5)
    c = Caozuolei()  # 注册乐玩
    c.Set_Dict(0, 'test3.txt')
    x = [[150, 290, 1], [270, 280, 2], [380, 215, 3], [490, 215], 4, [719, 285, 5], [80, 501, 6]]
    for aa in range(2, 3):
        time.sleep(1.5)  # 选一个任务
        c.LeftClick(x[aa][0], x[aa][1])  # 441, 310
        time.sleep(0.015)
        c.LeftClick(x[aa][0], x[aa][1])  # 单机两下鼠标左键0
        time.sleep(1.8)
        c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能

        # d
        # 女气功的操作流程，从选人物到进入图，在到刷图
        time.sleep(5)
        c.movingfigur_Down(0.95)  # 向下移动，移动一秒

        time.sleep(0.5)  # 睡眠0.5秒
        c.movingfigur_right(9)  # 向右移动， 移动8秒，

        # c.movingfigur_up(0.5)  # 向上移动， 移动0.15秒，
        dt.press('up')
        time.sleep(1.5)  # 睡眠1.5秒
        for i in range(10):
            time.sleep(0.25)  # 睡眠1.5秒
            dt.press('left')  # 向上移动， 移动0.15秒，

        time.sleep(0.5)  # 睡眠1.5秒

        dt.press('right')  # 向右移动， 移动1秒，
        # dt.press('right')  # 向右移动， 移动1秒，

        time.sleep(3)  # 睡眠1.5秒

        dt.press('space')  # 单击空格操作
        time.sleep(1.5)  # 睡眠1.5秒gdf
        if aa == 0:
            # c.nvQiGong(28, 0.54, 0.26, 0)#2p 睡眠不足十
            # c.nvQiGong(26, 0.64, 0.2, 0)  # 1p 气功师很烂丶
            c.nvQiGong(1, 0.54, 0.26, 0)  # 气功师该加强了
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(390, 500)  # 单机鼠标左键
            continue
        elif aa == 1:
            # c.zhaohuan(28, 0.05, 0.26, 0)#2p s睡眠不足s
            # c.kuangzhanshi(26, 0.21, 0.23, 0)#1p 狂战士
            c.nvQiGong(8, 0.48, 0.26, 0)  # 气功师该加强了
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(390, 500)  # 单机鼠标左键
            continue
        elif aa == 2:
            # c.nvQiGong(26, 0.56, 0.26, 0)  # 2p ll1ll数据i
            c.nvQiGong(28, 0.48, 0.2, 0)  # 1p 气功师狠烂

            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(390, 500)  # 单机鼠标左键
            continue
        elif aa == 3:
            c.nanQiGong(28, 0)  # 1p  男气功
            # c.nvQiGong(28,0.54,0.26,0)# 2p 睡眠不足丶

            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(390, 500)  # 单机鼠标左键
            break
    '''
    time.sleep(1.5)  # 选一个任务
    c.LeftClick(x[0][0], x[0][1])  # 441, 310
    time.sleep(0.015)
    c.LeftClick(150, 290)  # 单机两下鼠标左键
    time.sleep(1.8)
    c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能

    # ----
    # 女气功的操作流程，从选人物到进入图，在到刷图
    time.sleep(5)
    c.movingfigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒
    c.movingfigur_right(9)  # 向右移动， 移动8秒，

    # c.movingfigur_up(0.5)  # 向上移动， 移动0.15秒，
    dt.press('up')
    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.45)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，
    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(0.01)  # 睡眠1.5秒
    c.zhaohuan(28, 0.05, 0.26, 0)
    '''
    # c.nanQiGong(20,0)
    # c.nvQiGong(28,0.54,0.26,0)#睡眠不足数据0
    # c.zhaohuan(28, 0.05, 0.26, 1)#召唤数据i
    # c.nvQiGong(28, 0.54, 0.26, 0)  # 睡眠不足十数据
    # c.nvQiGong(18, 0.56, 0.26, 0)  # ll1ll数据i
    # c.nvQiGong(26, 0.54, 0.2, 0)  # 气功师很烂丶
    # c.nvQiGong(28, 0.48, 0.2, 0)  # 气功师狠烂
    # c.nvQiGong(8, 0.54, 0.26, 0g)  # 气功师该加强了
    # c.nvQiGong(8, 0.54, 0.32, 0)  # 气功师运气
    # c.kuangzhanshi(24,0.21,0.23,0)
    # c.nvQiGong(26, 0.54, 0.26, 0)  # 气功师不足丶

    # for i in range(1,10000):
    #     sleep(1)
    #     z=c.FindStr(x1=0,
    #               y1=0,
    #               x2=1000,
    #               y2=1000,
    #               string="不足",
    #               color_format="#422",
    #               sim=0.8,
    #               isbackcolor=0)
    #     if z!=0:
    #         x=z[0]
    #         y=z[1]+131
    #         print('x={},y={}'.format(x, y))
    #     else:
    #         print(0)

    # c.lw.MoveWindow(c.hwnd, 0, 0, 0, 0)  # 移动窗口，抢两个零是xy，后两个是窗口高度和宽度，默认为0不生效
    # for i in range(1, 10000):
    #     sleep(1)
    #     z = c.FindStr(x1=0,
    #                   y1=0,
    #                   x2=1000,
    #                   y2=1000,
    #                   string="挑战者",
    #                   color_format="#422",
    #                   sim=0.8,
    #                   isbackcolor=0)
    #     if z != 0:
    #         x = z[0] + 68
    #         y = z[1] + 135
    #
    #         print('x={},y={}'.format(x, y))
    #     else:
    #         for j in range(0, 1):
    #             sleep(1)
    #             z = c.FindStr(x1=0,
    #                           y1=0,
    #                           x2=1000,
    #                           y2=1000,
    #                           string="不足",
    #                           color_format="#422",
    #                           sim=0.8,
    #                           isbackcolor=0)
    #             if z != 0:
    #                 x = z[0]
    #                 y = z[1] + 131
    #                 print('x={},y={}'.format(x, y))
    #             else:
    #                 print(0)
    #                 break

    # c.lw.MoveTO(z[0],z[1])

    # c.Set_Dict(0, "测试2.txt")
    # Caozuolei().FuBen_INFO1()
    # c.Set_Dict(0, "测试2.txt")
    # c.kuangzhanshi(28,0)
    # c.nvQiGong(28,0.46,0.245,0)

    # if Caozuolei1().Find_Ocr(
    #     x1 = 0,
    #     y1 = 0,
    #     x2 = 1200,
    #     y2 = 1200,
    #     color_format= "#360",
    #     sim = 0.95,
    #     linesign = "五陵",
    #     isbackcolor = 0) == 1:
    #     print("识别成功！")
    # else:
    #     print("识别失败")

    # '''

    sleep(random.randint(0, 3))  # 随机睡眠一个小会儿
    c.UnBind()  # 解除绑定
