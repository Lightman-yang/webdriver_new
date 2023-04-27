import numpy as np
from PIL import Image
import multiprocessing
import os
import random
import time
from random import uniform
from time import sleep

import numpy as np
import pyautogui
import pydirectinput  as dt
import win32gui
from PIL import Image
from comtypes.client import CreateObject
from win32gui import FindWindow


class nvqigong():
    def NvQiGong(self, NvQiGongx, NvQiGongy, num_parameter, Restart_computer_parameter):
        '''步骤1 获取当前【鼠标坐标】'''
        # 获取当前鼠标【x y】坐标 309 118
        # time.sleep(5)
        # point = win32api.GetCursorPos()
        # print(point)
        # 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
        # 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
        dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发

        hwnd = win32gui.WindowFromPoint((NvQiGongx, NvQiGongy))  # 请填写 x 和 y 坐标
        print(hwnd)
        time.sleep(1)
        # 通过句柄将窗口放到最前
        # win32gui.SetForegroundWindow("句柄值")
        # dpyautogui.press('alt')
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(3)
        '''188疲劳，一次费6点疲劳，'''
        time.sleep(2)
        # 绑定窗口句柄
        # 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
        # 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
        dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发

        hwnd1 = win32gui.WindowFromPoint((308, 444))  # 请填写 x 和 y 坐标
        print(hwnd)
        time.sleep(1)

        '''步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置'''
        # 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
        # left, top, right, bottom = win32gui.GetWindowRect('句柄值')
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        print(left, top, right, bottom)

        for i in range(1, 60):
            time.sleep(3.5)
            num = num_parameter  # num不能是奇数 运行几次
            move_seep = -0.277  # 57.7
            m_button = 'h'
            print(move_seep)
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 7):
                # print('right开始按下{}次'.format(j))
                if j == 2:
                    dt.press('f')
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 1:
                    dt.press('t')
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.4 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 3:
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.9 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('g')
                    time.sleep(1.2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.2 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('h')
                    time.sleep(1.2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.0075)  # 按下两秒
                    dt.press('f')
                    time.sleep(1.2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('g')
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(3)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键


                elif j == 6:  # 奇数 反之偶数
                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.01)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(0.013)  # 按下两秒
                    dt.press('up')  # 像上按一下
                    dt.press('g')
                    time.sleep(0.45)
                    dt.press(m_button)
                    dt.press('f')
                    time.sleep(6)  # 按下两秒
                    z = 1
                    for z in range(1, 3):
                        time.sleep(0.5)  # 按下两秒
                        # dt.press('down')  # 像下按一下
                        dt.press('a')
                    time.sleep(2)  # 按下两秒
                    dt.press('0')
                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == 20 or i == 25 or i == num:
                            time.sleep(2)  # 按下两秒
                            dt.press('a')
                            time.sleep(1)  # 按下两秒
                            dt.press('space')
                            time.sleep(1.5)
                            dt.press('left')
                            time.sleep(1.5)
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
                    time.sleep(5)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 8
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

        # 通过句柄将窗口放到最前
        # win32gui.SetForegroundWindow("句柄值")
        # dpyautogui.press('alt')
        win32gui.SetForegroundWindow(hwnd)
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
            # self.lw.MoveTo((self.lw.x()+55),(self.lw.y()+124))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55), '+', "纵向坐标为：", '+', (self.lw.y() + 124), '+ ', "序号为：", '+',
                  self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
        else:
            print("没有！")

    def thread11(self):
        for z in range(1, 100000):
            nvqigong().Find_Pic(
                x1=0,
                y1=0,
                x2=600,
                y2=800,
                pic_name='选区者22.bmp',
                delta_color='25AB5A',
                sim=0.95,
                dir=0,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            sleep(random.randint(0, 2))  # 随机睡眠一个小会儿


if __name__ == '__main__':
    c = nvqigong()
    # nvqigong().thread11()
    # threads = [threading.Thread(target=nvqigong().NvQiGong(309, 118, 16, 0)),threading.Thread(target=nvqigong().thread11())]
    # # threads = [threading.Thread(target=nvqigong().NvQiGong(309, 118, 16, 0)),threading.Thread(target=thread11()),]
    # for i in threads:
    #     i.start()
    # zz = multiprocessing.Process(target=nvqigong().NvQiGong(309, 118, 16, 0))
    zzz = multiprocessing.Process(target=nvqigong().thread11(), daemon=True)
    zzz.start()
    # zz.start()
