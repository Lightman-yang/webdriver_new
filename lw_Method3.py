import os
import random
import time
from random import uniform
from time import sleep

import pydirectinput  as dt
import win32gui
from comtypes.client import CreateObject
from win32gui import FindWindow


class Caozuolei():
    time.sleep(2)
    # 绑定窗口句柄
    # 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
    # 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
    dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发

    hwnd1 = win32gui.WindowFromPoint((308, 444))  # 请填写 x 和 y 坐标
    print(hwnd1)
    time.sleep(1)

    '''步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置'''
    # 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
    # left, top, right, bottom = win32gui.GetWindowRect('句柄值')
    left, top, right, bottom = win32gui.GetWindowRect(hwnd1)
    print(left, top, right, bottom)

    # 通过句柄将窗口放到最前
    # win32gui.SetForegroundWindow("句柄值")
    # dpyautogui.press('alt')
    win32gui.SetForegroundWindow(hwnd1)
    time.sleep(2)

    def __init__(self):
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


if __name__ == '__main__':
    time.sleep(2)
    c = Caozuolei()  # 注册乐玩

    # ------------------------------------------------------------------------------------------>/
    # point_all=[[249,249],[378,452]]
    # print('点击坐标', x11, y11, '游戏坐标', left, top, right, bottom, '鼠标停放位置', point)
    # x22, y22=c.Coordinate_point(point_all[0][0],point_all[0][1]) #定位第二个人物坐标
    # print(x22, y22)
    # dt.move(x22, y22,duration=3)
    time.sleep(1.5)
    c.LeftClick(270, 280)  # 441, 310
    time.sleep(0.015)
    c.LeftClick(270, 280)  # 单机两下鼠标左键
    time.sleep(1.5)
    # c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能

    # ------------------------------------------------------------------------------------------>//
    # 女气功的操作流程，从选人物到进入图，在到刷图
    time.sleep(5)
    c.movingfigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒
    c.movingfigur_right(9)  # 向右移动， 移动8秒，

    c.movingfigur_up(0.15)  # 向上移动， 移动0.15秒，

    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.25)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(3)  # 睡眠1.5秒
    from python_v2023nvqigong import nvqigong

    nvqigong().NvQiGong(309, 118, 28, 0)
    # '''
    # ------------------------------------------------------------------------------------------->>///
    time.sleep(2)
    # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
    c.KeyPress1(27)  # 案件esc建
    # 425, 532 选人位置 424, 533
    time.sleep(3)
    c.LeftClick(390, 500)  # 单机鼠标左键

    # -------------------------------------------------------------------->/1
    # x22, y22 = c.Coordinate_point(point_all[1][0], point_all[1][1])  # 定位第3个人物坐标,狂战士
    # dt.move(x22, y22, duration=3)
    time.sleep(2)
    c.LeftClick(380, 215)  # 单机鼠标左键441, 310
    time.sleep(0.015)
    c.LeftClick(380, 215)  # 单机两下鼠标左键
    time.sleep(1.5)
    # c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能

    # -------------------------------------------------------------------->//2
    # 气功师二号的操作流程，从选人物到进入图，在到刷图
    time.sleep(5)
    c.movingfigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒
    c.movingfigur_right(9)  # 向右移动， 移动8秒，

    # c.movingfigur_up(0.15)  # 向上移动， 移动0.15秒，

    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.45)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(3)  # 睡眠1.5秒
    # from DXC_zhaohuan import DXCzhaohuan
    #
    # DXCzhaohuan().zhaohuan(309, 118, 30, 0)
    from python_v2023nvqigong import nvqigong

    nvqigong().NvQiGong(309, 118, 28, 1)
    time.sleep(3)  # 睡眠1.5秒

    # --------------------------------------------------------------------->///3
    time.sleep(2)
    # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
    c.KeyPress1(27)  # 案件esc建
    # 425, 532 选人位置 424, 533
    time.sleep(3)
    c.LeftClick(390, 500)  # 单机鼠标左键

    # ------------------------------------------------------------------------>/
    # x22, y22 = c.Coordinate_point(point_all[1][0], point_all[1][1])  # 定位第4个人物坐标
    # dt.move(x22, y22, duration=3)
    time.sleep(2)
    c.LeftClick(490, 215)  # 单机鼠标左键441, 310
    time.sleep(0.015)
    c.LeftClick(490, 215)  # 单机两下鼠标左键
    time.sleep(1.5)
    # c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能
    # ------------------------------------------------------------------------->//

    # 女气功的操作流程，从选人物到进入图，在到刷图
    time.sleep(5)
    c.movingfigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒
    c.movingfigur_right(9)  # 向右移动， 移动8秒，

    # c.movingfigur_up(0.15)  # 向上移动， 移动0.15秒，

    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.45)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(3)  # 睡眠1.5秒
    nvqigong().NvQiGong(309, 118, 23, 0)
    # ------------------------------------------------------------------------>///

    # -------------------------------->/
    time.sleep(2)
    c.KeyPress1(27)  # 案件esc建
    time.sleep(3)
    c.LeftClick(390, 500)  # 单机鼠标左键
    # -------------------------------->//
    # 第五个选人位置   第五位  第五个选人位置   第五位
    time.sleep(1.5)
    c.LeftClick(719, 285)  # 441, 310
    time.sleep(0.015)
    c.LeftClick(719, 285)  # 单机两下鼠标左键
    time.sleep(2)
    # ------------------------------------>///

    #  -奶妈的操作流程，从选人物到进入图，在到刷图-
    time.sleep(5)
    c.movingfigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒
    c.movingfigur_right(9)  # 向右移动， 移动8秒，

    # c.movingfigur_up(0.15)  # 向上移动， 移动0.15秒，

    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.45)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(3)  # 睡眠1.5秒
    # from python_NaiMA import DXC_NaiMA  # 奶妈
    # DXC_NaiMA().DXCNaiMA(309, 118, 30, 0)

    nvqigong().NvQiGong(309, 118, 23, 0)  # 女气功

    # from DXC_zhaohuan import DXCzhaohuan #召唤
    #
    # DXCzhaohuan().zhaohuan(309,118,26,1)

    sleep(random.randint(0, 3))  # 随机睡眠一个小会儿
    c.UnBind()  # 解除绑定
