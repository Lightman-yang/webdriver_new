import os
import random
import time
from comtypes.client import CreateObject
from ctypes import WinDLL
from random import uniform
from time import sleep
from win32com import client
from win32con import NULL
from win32gui import FindWindow


class Caozuolei():
    # 绑定窗口句柄
    def __init__(self):
        self.hwnd = FindWindow("LaunchUnrealUWindowsClient", None)
        self.path = os.getcwd()
        try:
            self.lw = CreateObject('lw.lwsoft3')
        except OSError:
            # print(path)
            os.system(r'regsvr32 /s %s\lw.dll' % self.path)
            self.lw = CreateObject('lw.lwsoft3')
        # 绑定窗口
        self.BindWindow()

    def BindWindow(self):
        self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        self.lw.BindWindow(self.hwnd, 0, 0, 0, 0, 0)
        # self.lw.EnableRealMouse(2,20,30)
        self.lw.SetDict(0, "find.txt")
        print("find")

        print("执行过了")

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
    def LeftClick(self, x1, y1, xr, yr, delay=uniform(0.3, 0.5)):
        self.lw.SetWindowState(self.hwnd, 12)  # 激活窗口
        x = x1 + random.randint(1, xr)
        y = y1 + random.randint(1, yr)
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


# 080037F840018002BFE37F8E06180C30192030406080C11F82000$行$0.0.66$15.14.15.14
if __name__ == '__main__':
    c = Caozuolei()  # 注册乐玩
    c.KeyPress1(70)  # 案件F建
    time.sleep(3)

    for i in range(10):
        if c.FindStrFastEx(124, 848, 238, 892, "拍卖行", "#408", 1.0, 0):
            c.LeftClick(c.x, c.y, 2, 2)
            break
        time.sleep(0.2)
    sleep(random.randint(0, 10))  # 随机睡眠一个小会儿
    c.UnBind()  # 解除绑定
