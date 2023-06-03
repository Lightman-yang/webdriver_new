import os
import random
import smtplib
import time
# import pandas as pd
from email.header import Header
from email.mime.text import MIMEText
from random import uniform
from time import sleep  # 导入时间休眠函数

import numpy as np
import openpyxl
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

    # 发送邮件
    def send_mails_QQsmtp(self, from_mail, to_mail, note_content, apartment_name, subject,
                          user_name, mail_host, mail_port, mymail_user, mymail_pwd):
        print(f'正在向{to_mail}发生邮件......')
        # mail msg 设置

        msg = MIMEText(note_content, 'plain', 'utf-8')
        msg['From'] = apartment_name
        msg['To'] = user_name
        msg['Subject'] = Header(subject, 'utf-8')
        with smtplib.SMTP_SSL(mail_host, mail_port) as smtObj:
            # 登陆发件人邮箱（公寓财务处邮箱）
            smtObj.login(mymail_user, mymail_pwd)
            # 发送
            smtObj.sendmail(from_mail, to_mail, msg.as_string())
            print('邮件成功发送！')

    def youjian(self):
        user_info = ['286224275@qq.com']

        apartment_dict = {
            'from_mail': '1074952101@qq.com',
            # 密码pwd
            'pwd': 'uewdydfgwvakghhf',
            'sub': '通知提醒',
            'apartment_name': '1074952101@qq.com'
        }
        """查询用户信息发送邮件"""
        # 使用邮件服务商提供的SMTP服务，需要设置服务器/端口号/用户名/口令（即授权码）等
        # QQmail_host, QQmail_port = 'smtp.qq.com', 465
        QQmail_host, QQmail_port = 'smtp.qq.com', 465
        QQmail_user = apartment_dict.get('from_mail')
        QQmail_pwd = apartment_dict.get('pwd')
        apartment_name = apartment_dict.get('apartment_name')
        sub = apartment_dict.get('sub')
        to_mail = user_info[0]  # 收件邮箱
        user_name = user_info[0]  # 亲爱的xxx用户xx
        # room_no = user_info[2]  # 房间号
        note_content = f'亲爱的{1}，你好：系统显示，游戏已经崩溃了！\
                                 \n{apartment_name}\
                                 \n崩溃时间为{time.strftime("%Y-%m-%d %H:%M-%S秒", time.localtime())}！'
        self.send_mails_QQsmtp(QQmail_user, to_mail, note_content, apartment_name, sub,
                               user_name, QQmail_host, QQmail_port, QQmail_user, QQmail_pwd)

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

    # 切换字库
    def Use_Dict(self, index):

        ret = self.lw.UseDict(index)
        if ret == 1:
            print("切换字库{}成功！".format(index))
            return 1

        else:
            print("切换字库{}失败！".format(index))
            return 0

    def FuBen_INFO1(self):  # 副本地图信息数据实时获取
        time.sleep(0.4)
        # self.Use_Dict(1)
        # c.Set_Dict(0, "测试2.txt")
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
        self.Use_Dict(1)
        # c.Set_Dict(0, "测试2.txt")
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
        self.Use_Dict(1)
        # c.Set_Dict(0, "测试2.txt")
        while True:
            time.sleep(0.15)
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
                dt.press('.')
                time.sleep(2)
                print("再次挑战", 1)
                return 1


            else:
                print("再次挑战", 0)
                return 0

    def FuBen_INFO(self):  # 副本地图信息数据实时获取
        self.Use_Dict(1)
        while True:
            time.sleep(0.15)
            aa = self.Find_Ocr(
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
                return 100
                # continue
            elif "第一关" in aa and "开门" not in aa:
                print('第一关')
                return 1
                # continue
            elif "开门" in aa:
                print('第二关')
                return 2
                # continue
            elif "凹凸" in aa and "星星" not in aa:
                print("在第三关凹凸")
                return 3
            elif "大鱼海棠" in aa or "夜空下" in aa:
                print("在第四关")
                return 5
            elif "星星" in aa:
                print("在第5关")
                return 6
            elif "花花" in aa and "好绿" not in aa:
                print("在6关")
                return 7
            elif "好绿" in aa or (("好绿" in aa) and ("花花" in aa)):
                print("在7关")
                return 8
            elif "最后" in aa and "再次挑战" not in aa:
                print("在boss房间")
                return 9
            elif "再次挑战" in aa:
                print("通关完成")
                return 10
            else:
                print("0,没找到")
                return 0

    def FuBen_INFO11(self):  # 进图校验是否选择“永恒之光研究所”

        self.Use_Dict(0)
        while True:
            time.sleep(0.15)
            aa = self.Find_Ocr(
                x1=31,
                y1=245,
                x2=260,
                y2=33,
                color_format="#331",
                sim=0.8,
                linesign=" ",
                isbackcolor=1)
            if "永恒之光" in aa:

                print("永恒之光")

                return 1
            else:
                dt.press('up')
                break

    def FuBen_INFOxx(self, num):

        if num == 1:
            # self.forxunhuan(601,478)
            self.forxunhuan()
            return
        elif num == 2:
            # self.forxunhuan(202,500)
            self.forxunhuan()
            return
        elif num == 3:
            # self.forxunhuan(202, 520)
            self.forxunhuan()
            return
        elif num == 4:
            self.forxunhuan()
            # self.forxunhuan(530, 485)
            return
        elif num == 5:
            self.forxunhuan()
            # self.forxunhuan(415, 420)
            return
        elif num == 6:
            dt.press('up')

            time.sleep(0.013)  # 按下两秒
            dt.keyDown('up')  # ：模拟按键按下
            time.sleep(1.35)  # 按下19秒
            dt.keyUp('up')  # ：模拟按键松开按键
            # self.forxunhuan(493, 490)
            self.forxunhuan()
            return
        elif num == 7:
            # self.forxunhuan(131, 393)
            self.forxunhuan()
            dt.press('right')

            time.sleep(0.013)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.56)  # 按下19秒
            dt.keyUp('right')  # ：模拟按键松开按键
        else:
            # self.youjian()  # 发送邮件

            print('FuBen_INFOxx什么也没有找到')
            time.sleep(10)

    def FuBen_INFO6(self, b=0, c=1):  # 副本地图信息数据实时获取
        self.Set_Dict(0, 'test3.txt')
        self.Use_Dict(0)
        # c.Set_Dict(0, "test3.txt")
        time.sleep(2)
        cc = c
        while True:
            cc = cc + 1

            aa = self.Find_Ocr(
                x1=392,
                y1=63,
                x2=853,
                y2=574,
                color_format="#380",
                sim=0.88,
                linesign=" ",
                isbackcolor=0)
            if "开洞" in aa:
                print('开洞')
                return
            elif cc == 6 and "开洞" not in aa and b == 1:
                dt.press('right')
                dt.press('alt')

                continue
            elif (cc == 20 or cc == 25) and "开洞" not in aa:
                dt.press('alt')
                continue
            elif 20 > cc > 7 and "开洞" not in aa:
                dt.press('right')
                continue
            elif cc <= 7 and "开洞" not in aa:
                print("9等待9")
                dt.press('g')
                time.sleep(0.075)
                dt.press('y')
                time.sleep(1)
                continue
            else:
                aa1 = self.Find_Ocr(
                    x1=0,
                    y1=0,
                    x2=800,
                    y2=800,
                    color_format="#380",
                    sim=0.88,
                    linesign=" ",
                    isbackcolor=0)
                if "开洞" in aa1:
                    print('开洞')
                    return
                else:
                    self.youjian()
                    return

    def nvQiGong(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1=0.75,
                 hh2=0.75):
        # 女气功 花花
        print(num_parameter, move_seepx, move_seepy, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1, hh2)
        # 定位坐标[606,401,75,499, 502,481, 460,481, 360,454]
        # self.forxunhuan(460,481)
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
            a_error = 0
            Restart_computer = Restart_computer_parameter  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑
            for j in range(1, 9):
                # print('right开始按下{}次'.format(j))
                # a_error = 0
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
                    time.sleep(2.6 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('left')  # ：模拟按键按下
                    time.sleep(0.15)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.5)
                    dt.press('9')
                    time.sleep(1.5)

                    if self.FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:

                        time.sleep(1.35)
                        self.FuBen_INFO6()
                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键

                        if self.FuBen_INFO() == 1:

                            self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                            time.sleep(1)  # 按下两秒
                            dt.keyDown('right')  # ：模拟按键按下 向下
                            time.sleep(1.5 + move_seep1)
                            dt.keyUp('right')  # ：模拟按键松开按键


                        else:
                            pass

                elif j == 2:
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    # self.Find_srt("熟练者", "#422", "功师", "#422")
                    dt.press('y')
                    time.sleep(0.65)
                    dt.press('g')
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    dt.keyDown('right')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(0.75)
                    dt.press('v')
                    time.sleep(0.5)  # 按下两秒
                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    print('二操作9成功')
                    # time.sleep(1.2)
                    # Caozuolei().FuBen_INFO1()

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
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
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6()
                    time.sleep(0.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('left')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(3.9 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('g')
                    time.sleep(0.75)
                    dt.press('f')
                    time.sleep(0.75)
                    dt.press('y')
                    self.FuBen_INFO6(1)
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.7)
                    dt.press('d')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('f')
                    time.sleep(0.7)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('g')
                    time.sleep(0.75)
                    dt.press('y')
                    time.sleep(0.9)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('y')
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.45 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(1)
                    self.FuBen_INFO6()
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.7 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.05)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.55 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(0.65 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键
                    dt.press('t')
                    time.sleep(1.5)
                    dt.press('c')

                    time.sleep(0.5)
                    dt.press('d')
                    time.sleep(0.5)
                    self.FuBen_INFO6()
                    time.sleep(0.7)
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    dt.press('9')
                    time.sleep(0.75)
                    self.FuBen_INFO1()
                    time.sleep(1)
                    time.sleep(0.56)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键


                elif j == 6:
                    time.sleep(0.75)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.8 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('g')
                    time.sleep(1)
                    # self.Find_srt(aa1, bb1, cc1, dd1)
                    dt.keyDown('right')  # ：模拟按键按下 向下
                    time.sleep(0.6 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6(c=6)
                    time.sleep(0.1)
                    dt.press('9')
                    time.sleep(0.75)
                    self.FuBen_INFO1()
                    time.sleep(0.5)  # 按下两秒
                    # Caozuolei().FuBen_INFO1()

                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数
                    time.sleep(0.75)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.8 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(1)
                    time.sleep(0.7)  # 按下19秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('d')

                    time.sleep(1.2)
                    self.FuBen_INFO1()

                    time.sleep(1.5)

                    # self.forxunhuan(aa1, bb1, cc1, dd1)

                    dt.press('9')
                    time.sleep(0.5)
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
                    time.sleep(0.75)  # 按下19秒
                    dt.press('f')
                    time.sleep(0.89)  # 按下19秒
                    dt.press('e')
                    time.sleep(0.89)  # 按下19秒
                    dt.press('r')
                    time.sleep(0.75)  # 按下两秒
                    self.FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            # from python_findpicture import Caozuolei1
                            self.sellGoods_xy()  # 点击一键出售按钮
                            print('等待3')
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
                        dt.press('.')
                        dt.press('f12')
                        time.sleep(2)
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

    def kuangzhanshi(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter,aa1, bb1, cc1,
                     dd1, hh1=0.75,hh2=0.75):
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

                    dt.press('left')
                    dt.press('y')
                    time.sleep(0.5)




                    if self.FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:
                        self.FuBen_INFO6()
                        dt.press('9')
                        time.sleep(1.5)
                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键
                        if self.FuBen_INFO() == 1:
                            self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                            time.sleep(1)  # 按下两秒
                            dt.keyDown('right')  # ：模拟按键按下 向下
                            time.sleep(1.5 + move_seep1)
                            dt.keyUp('right')  # ：模拟按键松开按键
                        else:
                            pass
                elif j == 2:

                    time.sleep(0.7)
                    dt.press('t')
                    time.sleep(0.3)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    time.sleep(0.3)
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('g')
                    dt.press('right')  # ：模拟按键按下
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 3:

                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.68 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.5)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.15 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')



                    time.sleep(1)
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.75 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()

                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('left')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(3.7 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('f')
                    time.sleep(0.75)
                    dt.press('g')
                    self.FuBen_INFO6(1)
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 4:
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('y')
                    time.sleep(0.75)

                    dt.press('t')
                    time.sleep(0.7)
                    dt.press('g')

                    time.sleep(1.5)
                    dt.press('y')
                    time.sleep(0.8)  # 按下两秒


                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.45 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1)  # 按下两秒
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.03)
                    dt.keyDown('down')  # ：模拟按键按下 向下

                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.9 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.9 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    dt.keyDown('left')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('left')  # ：模拟按键松开按键
                    time.sleep(0.7)
                    dt.press('y')
                    time.sleep(0.7)
                    self.FuBen_INFO6()

                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    dt.press('9')
                    time.sleep(0.7)
                    self.FuBen_INFO1()
                    time.sleep(1)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.95 + move_seep1)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.6)
                    dt.keyDown('right')  # ：模拟按键按下 向下

                    time.sleep(0.9 + move_seep1)

                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.6)
                    dt.keyUp('right')
                    dt.press('g')

                    time.sleep(1)  # 按下两秒



                    dt.press('right')
                    time.sleep(0.007)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.55 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按
                    self.FuBen_INFO1()
                    dt.press('9')
                    time.sleep(1)  # 按下两秒


                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    time.sleep(1.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数




                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(0.88)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('g')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
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
                    time.sleep(1.6 + move_seep)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('t')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('f')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('g')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('v')
                    time.sleep(0.75)  # 按下19秒
                    dt.press('q')

                    time.sleep(2)  # 按下两秒
                    self.FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            #from python_findpicture import Caozuolei1
                            self.sellGoods_xy()  # 点击一键出售按钮
                            print('等待4')
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
                        dt.press('.')
                        dt.press('f12')
                        time.sleep(1)
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

    def nanQiGong(self, num_parameter, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1=0.75,
                 hh2=0.75):
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
                    dt.press('t')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('h')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('s')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.85 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键



                    dt.press('left')
                    dt.press('y')
                    time.sleep(0.5)

                    if self.FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:
                        self.FuBen_INFO6()
                        dt.press('9')
                        time.sleep(0.75)
                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.45)
                        dt.keyUp('down')  # ：模拟按键松开按键
                        if self.FuBen_INFO() == 1:
                            self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)


                            dt.keyDown('right')  # ：模拟按键按下 向下
                            time.sleep(1.5)
                            dt.keyUp('right')  # ：模拟按键松开按键
                        else:
                            pass


                elif j == 2:

                    time.sleep(0.1)
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('s')
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')

                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.015)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下 向下
                    time.sleep(0.7)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(0.75)
                    dt.press('y')
                    time.sleep(0.5)  # 按下两秒
                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    print('二操作9成功')
                    # time.sleep(1.2)
                    # Caozuolei().FuBen_INFO1()

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键






                elif j == 3:
                    time.sleep(0.1)
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
                    dt.press('e')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('e')
                    # time.sleep(0.75)  # 按下两秒
                    # dt.press('9')
                    time.sleep(0.7)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.015)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.8)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6()
                    time.sleep(0.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('left')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(3.9 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.press('y')
                    time.sleep(0.75)
                    dt.press('f')
                    time.sleep(0.75)
                    dt.press('s')
                    self.FuBen_INFO6(1)
                    dt.press('9')
                    time.sleep(1)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键




                elif j == 4:
                    time.sleep(0.1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.75 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.0075)  # 按下两秒
                    dt.press('e')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('s')

                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.45 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    time.sleep(1)
                    self.FuBen_INFO6()
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.35 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.6)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(0.8 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键

                    dt.press('t')
                    time.sleep(1.5)  # 按下两秒
                    dt.press('y')
                    time.sleep(1.25)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    time.sleep(0.7)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.85 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 6:
                    time.sleep(0.1)
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

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.7 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按
                    dt.press('9')
                    time.sleep(1.2)

                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    time.sleep(0.5)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0175)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按

                    # c=1



                elif j == 7:  # 奇数 反之偶数

                    time.sleep(0.75)
                    dt.keyDown('up')  # ：模拟按键按下 向下
                    time.sleep(1.3 + move_seep)
                    dt.keyUp('up')  # ：模拟按键松开按键

                    time.sleep(0.2)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.8)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.4)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('d')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    time.sleep(1)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.6)  # 按下19秒
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
                    self.FuBen_INFO2()

                    dt.press('0')
                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒
                            #from python_findpicture import Caozuolei1
                            self.sellGoods_xy()  # 点击一键出售按钮
                            print('等待5')
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
                        dt.press('.')
                        dt.press('f12')
                        time.sleep(0.75)
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

    def zhaohuan(self, num_parameter, move_seepx, move_seepy, Restart_computer_parameter, aa1, bb1, cc1, dd1, hh1=0.75,
                 hh2=0.75):
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
                    time.sleep(0.35)  # 按下两秒
                    dt.press('t')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('s')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('t')
                    dt.press('g')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('f')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(1.75)  # 按下两秒
                    dt.press('y')
                    time.sleep(0.75)  # 按下两秒
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    if self.FuBen_INFO3() == 1:
                        j = 8
                        i = num
                        print('测试')
                        break
                    else:
                        self.FuBen_INFO6()
                        dt.keyDown('down')  # ：模拟按键按下 向下
                        time.sleep(0.5 + move_seep1)
                        dt.keyUp('down')  # ：模拟按键松开按键

                        dt.press('9')

                        if self.FuBen_INFO() == 1:

                            self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                            time.sleep(1)  # 按下两秒
                            dt.keyDown('right')  # ：模拟按键按下 向下
                            time.sleep(2 + move_seep1)
                            dt.keyUp('right')  # ：模拟按键松开按键
                        else:
                            pass

                elif j == 2:

                    time.sleep(1)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(1 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键
                    dt.press('s')
                    time.sleep(3)
                    time.sleep(1.35)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO6()
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    time.sleep(2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.15 + move_seep)
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
                    time.sleep(1)  # 按下两秒

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.4 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    # Caozuolei().FuBen_INFO6(
                    dt.press('9')
                    time.sleep(1.2)
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('left')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(3.95 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键
                    time.sleep(1.5)
                    self.FuBen_INFO6()

                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    time.sleep(1)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.7 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(3.1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 4:
                    time.sleep(1)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.5 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                    dt.press('s')
                    time.sleep(0.75)
                    dt.press('w')

                    time.sleep(1)
                    dt.press('s')
                    time.sleep(0.75)
                    dt.press('f')

                    time.sleep(1)
                    time.sleep(1.35)
                    dt.press('9')
                    time.sleep(1.2)
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.4 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    self.FuBen_INFO1()
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1.8 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 5:
                    time.sleep(0.15)
                    dt.keyDown('down')  # ：模拟按键按下 向下
                    time.sleep(0.75 + move_seep1)
                    dt.keyUp('down')  # ：模拟按键松开按键

                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1 + move_seep)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.keyDown('up')  # ：模拟按键按下 向下gygygygy
                    time.sleep(1.68 + move_seep1)
                    dt.keyUp('up')  # ：模拟按键松开按键
                    dt.keyDown('left')  # ：模拟按键按下
                    time.sleep(1.14 + move_seep)
                    dt.keyUp('left')  # ：模拟按键松开按键
                    dt.press('r')
                    time.sleep(1.35)
                    self.forxunhuan(aa1, bb1, cc1, dd1, hh1, hh2)
                    dt.press('9')

                    self.FuBen_INFO1()
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
                    self.FuBen_INFO1()
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
                    self.FuBen_INFO1()

                    time.sleep(1)
                    dt.keyDown('up')  # ：模拟按键按下 向下.
                    time.sleep(0.3 + move_seep1)
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
                    time.sleep(0.1)  # 按下19秒
                    dt.press('ctrl')
                    time.sleep(0.8)  # 按下19秒
                    dt.press('g')
                    time.sleep(0.45)  # 按下19秒
                    dt.press('s')
                    time.sleep(2)  # 按下两秒
                    self.FuBen_INFO2()
                    dt.press('0')

                    time.sleep(1)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num // 2
                        if i == num_num or i == 10 or i == num:
                            time.sleep(5)  # 按下两秒

                            self.sellGoods_xy()  # 点击一键出售按钮
                            print('等待6')
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
                        dt.press('.')
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

    def excelboot01(self, nn):  # 参数是传几取列表（nn-1）行的数据
        zzzzz1 = []
        # data =openpyxl.load_workbook(wu)
        data = openpyxl.load_workbook(r"D:\webdriver_new\lw\game_name.xlsx")
        # 获取工作表 有三种方法
        zz1 = data.active  # 不知道表名称的 用这种
        # zz1=data['Sheet'] #知道表面的用第二种
        # zz1=data.get_sheet_by_name('Sheet1') #第三种不知道和第二种有什么区别
        # 获取表A1数据
        # z_max=zz1.max_row #获取最大行数
        # z_min=zz1.min_row #获取最小行数
        # c_min=zz1.max_column #获取最大数列
        # c_min = zz1.min_column  # 获取最小数列
        # cell.coordinate 定位数据
        # 获取行数nn
        max_row_num = zz1.max_row
        row_list2 = []
        for i in range(nn + 1, max_row_num + 1):  # nn代表从哪行开始取  第一行有标题，要去掉标题党，所有nn+1才是列表的值

            for row in zz1[i]:
                row_list2.append(row.value)
        print(row_list2[0:8])
        return row_list2[2:8]  # 取数据直接截取前6条数据 并返回给调用方

    def FindStr(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor):
        ret = self.lw.FindStr(x1, y1, x2, y2, string, color_format, sim, isbackcolor)
        if ret == 1:
            return self.lw.x(), self.lw.y()
        else:
            print('零')
            # dt.press('alt')
            return 0

    def Find_srt(self, usr_string1, usr_color_format1, usr_string2, usr_color_format2, usr_HH1=0.75,
                 usr_HH2=0.75):  # 人物坐标
        self.Use_Dict(0)
        print(usr_HH1, type(usr_HH1))
        b = 0
        while True:

            sleep(0.15)
            z = self.FindStr(
                x1=0,
                y1=0,
                x2=800,
                y2=600,
                string=usr_string1,  # "先驱者",  # "挑战者"
                color_format=usr_color_format1,  # "#422",  ##380
                sim=usr_HH1,
                isbackcolor=0)
            print(z, "<>")
            if z != 0:
                x = z[0] + 68
                y = z[1] + 100
                # xxyy[0:2] = x, y
                xxyy[0] = x
                xxyy[1] = y
                # xxyy[5] = 999
                # print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1],xxyy[2],xxyy[3]))
                print('人物坐标', z[0], '+', 68, '=', xxyy[0])
                return
            else:

                z = self.FindStr(
                    x1=0,
                    y1=0,
                    x2=800,
                    y2=600,
                    string=usr_string2,  # "不足",
                    color_format=usr_color_format2,  # "#422",
                    sim=usr_HH2,
                    isbackcolor=0)
                if z != 0:
                    x = z[0]
                    y = z[1] + 104
                    # xxyy[5] = 999
                    xxyy[0] = x
                    xxyy[1] = y
                    # print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]), ',?')
                    print('人物坐标', z[0], '+', 0, '=', xxyy[0])
                    return
                else:
                    b = b + 1
                    if b == 60:
                        self.youjian()
                        print('!!!')
                        return
                    elif 32 > b > 30:
                        dt.press('right')
                        dt.press('alt')
                        continue
                    else:
                        print(b)
                        break
                    # print(0, xxyy)
                    #
                    # print("从新找")
                    # continue

    def menzuobiao(self):  # 门坐标
        self.Use_Dict(0)
        while True:

            z = self.FindStr(
                x1=392,
                y1=63,
                x2=853,
                y2=574,
                string="开洞",  # "先驱者",  # "挑战者"
                color_format="#380",  # "#422",  ##380
                sim=0.8,
                isbackcolor=0)
            print(z, 'z')
            if z != 0:
                xxyy[2] = z[0] - 140
                xxyy[3] = z[1] + 65
                xxyy[4] = 88  # 找到数据传88
                # xxyy[2:2] = x, y
                print('开洞', z[0], '-', 140, '=', xxyy[2])
                print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                return
            else:
                print('测试', xxyy[0])
                if xxyy[3] == 4 and xxyy[0] > 500:

                    return
                elif xxyy[3] == 4 and xxyy[0] < 90:
                    dt.press('right')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(1)
                    dt.keyUp('right')  # ：模拟按键松开按键
                    return
                else:
                    return

    # 人物移动到地图某一个x，y坐标点
    def forxunhuan(self, aa, bb, cc, dd, hh1=0.75, hh2=0.75):  # ,aa,bb,cc,dd
        # self.Use_Dict(0)
        a = [1]
        num_ss = [0]
        while '真' not in a:

            print(' else #10', (a))
            self.Find_srt(aa, bb, cc, dd, hh1, hh2)
            # self.Find_srt("先驱者","#422", "不足", "#422")
            # # self.menzuobiao()
            # x, y, x1, y1, z, h = xxyy
            # # print('x=',x,'y=',y,x1,y1,z,h)
            # if -11 < (x-x1) < 11 and -11 < (y- y1)  < 11 and z==88 :
            #
            #     print((x-x1), 'y','外层循环')
            #     return
            # else:
            for j in range(1, 20):
                print(num_ss[0])
                self.menzuobiao()
                # self.Find_srt(aa1, bb1, cc1, dd1)
                time.sleep(1)

                x, y, x1, y1, z, h = xxyy
                print(xxyy)
                print((x - x1), (y - y1), '----')
                if h == 1000:
                    break
                elif (x - x1) < int(-80) and z == 88 and num_ss[0] == 0:  # 0
                    dt.press('right')
                    time.sleep(0.013)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.1)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键
                    print('#0,人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                    # self.Find_srt("熟练者", "#422", "功师", "#422")
                    num_ss[0] = 1
                    break

                elif int(x - x1) < -12 and z == 88 and num_ss[0] == 0:  # 1
                    # print((x - x1), 'x,1')
                    dt.press('right')
                    # time.sleep(0.1)  # 按下19秒
                    # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1],xxyy[2],xxyy[3]))
                    print("right,#1")
                    # self.Find_srt("熟练者", "#422", "功师", "#422")
                    num_ss[0] = 1
                    break
                elif int(x - x1) > 12 and z == 88 and num_ss[0] == 0:  # 2
                    # print((x - x1), 'x,2')
                    dt.press('left')
                    # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1],xxyy[2],xxyy[3]))
                    print("left,#2")
                    # self.Find_srt("熟练者", "#422", "功师", "#422")
                    num_ss[0] = 1
                    break

                elif int(y - y1) < -80 and z == 88 and num_ss[0] == 1:
                    dt.keyDown('down')  # ：模拟按键按下
                    time.sleep(0.4)  # 按下19秒
                    dt.keyUp('down')  # ：模拟按键松开按键
                    # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                    print("down,#3")
                    num_ss[0] = 0
                    break
                elif int(y - y1) > 80 and z == 88 and num_ss[0] == 1:  # 4
                    dt.keyDown('up')  # ：模拟按键按下
                    time.sleep(0.4)  # 按下19秒
                    dt.keyUp('up')  # ：模拟按键松开按键
                    print("down,#4")
                    num_ss[0] = 0
                    break
                elif int(y - y1) < -12 and z == 88 and num_ss[0] == 1:  # 5
                    # print((y- y1), 'y1')
                    dt.press('down')
                    print("down,#5")
                    num_ss[0] = 0
                    break

                elif int(y - y1) > 12 and z == 88 and num_ss[0] == 1:  # 6
                    # print((y- y1) , 'y2')
                    dt.press('up')
                    # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                    print("up,#6")
                    num_ss[0] = 0
                    break
                # elif 11 < int(y- y1) > -11 and z==88:
                #     print((y- y1) , 'y3')
                #    # continue
                # elif 11 > int(x - x1) > -11 and z==88:
                #     print((x - x1), 'x,3')
                #    # continu
                #     print((y - y1)>80)
                elif -12 <= (x - x1) <= 12 and -12 <= (y - y1) <= 12 and z == 88:  # 7
                    # print((x-x1), 'y？？？？？？')
                    # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                    print("up,#7")

                    a.append("真")
                    break
                elif num_ss[0] == 1:
                    num_ss[0] = 0
                    print(';;')
                    break
                elif num_ss[0] == 0:
                    num_ss[0] = 1
                    print(';')
                    break
                else:
                    if x > 600:  # 8
                        dt.keyDown('left')  # ：模拟按键按下
                        time.sleep(1)  # 按下19秒
                        dt.keyUp('left')  # ：模拟按键松开按键
                        # print((x-x1) , 'x', (y- y1), 'y','怎么回事')
                        # print('人物坐标{},{},dong门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                        print("up,#8")
                        break


                    else:
                        print(xxyy)
                        # self.youjian()
                        dt.press('right')
                        dt.press('alt')
                        print("up,#100")
                        break


if __name__ == '__main__':
    global xxyy
    xxyy = [1, 2, 3, 4, 99, 6]
    # 定位坐标[606,401,75,499,502,481,460,481,360,454]
    # c.forxunhuan(606, 401)
    # move_seep = -0.54  # 57.7   气功4.2  40.8
    # move_seep1 = -0.26
    # 睡眠不足十62.5%

    time.sleep(1.5)
    c = Caozuolei()  # 注册乐玩
    # dt.press('alt')
    print(1)
    # time.sleep(1000)

    c.lw.MoveWindow(c.hwnd, 1, 1, 0, 0)  # 移动窗口，抢两个零是xy，后两个是窗口高度和宽度，默认为0不生效
    # c.Set_Dict(1, '测试2.txt')
    # c.Set_Dict(0, 'test3.txt')
    #
    #
    # while True:
    #     c.FuBen_INFO()
    #     time.sleep(1)
    # else:
    #     pass
    c.Set_Dict(0, 'test3.txt')
    c.Set_Dict(1, '测试2.txt')

    # c.forxunhuan("熟练者", "#422", "功师", "#422")
    # c.forxunhuan("熟练者", "#410", "师很", "#140")
    print(1)

    # c.Find_srt("熟练者", "#422", "师很", "#422")
    # time.sleep(1000)

    # c.FuBen_INFOxx(3)
    # time.sleep(1)
    # c.forxunhuan(627,462)
    # c.Find_srt("熟练者", "#422", "功师", "#422")
    time.sleep(1)
    pvp = 2  # 1是1P 2是2p
    # x = [[150, 290, 1], [270, 280, 2], [380, 215, 3], [490, 215], 4, [719, 285, 5], [80, 501, 6]]
    x = [[134, 231, 1], [274, 258, 2], [412, 244, 3], [556, 247, 4], [691, 256, 5], [67, 464, 6], [204, 466, 7],
         [350, 487, 7]]
    for aa in range(0, 5):  # 打图设置

        time.sleep(1.85)  # 选一个任务
        c.LeftClick(x[aa][0], x[aa][1])  # 441, 310
        time.sleep(0.015)
        c.LeftClick(x[aa][0], x[aa][1])  # 单机两下鼠标左键0
        time.sleep(1.8)
        c.KeyPress1(190)  # 案件‘.’建，功能是隐藏技能和血功能

        # d
        # 女气功的操作流程，从选人物到进入图，在到刷图
        time.sleep(5)
        if x[aa][2] == 6:
            c.movingfigur_Down(0.65)  # 向下移动，移动一秒
        else:

            c.movingfigur_Down(0.95)  # 向下移动，移动一秒

        time.sleep(0.5)  # 睡眠0.5秒
        c.movingfigur_right(7.5)  # 向右移动， 移动8秒，

        # c.movingfigur_up(0.5)  # 向上移动， 移动0.15秒，

        dt.press('up')
        c.FuBen_INFO11()
        time.sleep(1.5)  # 睡眠1.5秒
        for i in range(10):
            time.sleep(0.25)  # 睡眠1.5秒
            dt.press('left')  # 向上移动， 移动0.15秒，

        time.sleep(0.5)  # 睡眠1.5秒
        dt.press('right')  # 向右移动， 移动1秒，
        dt.press('right')  # 向右移动， 移动1秒，
        # dt.press('right')  # 向右移动， 移动1秒，
        # dt.press('right')  # 向右移动， 移动1秒，
        if x[aa][2] == 4 and pvp == 2:
            pass
        else:
            dt.press('right')  # 向右移动， 移动1秒，
        # dt.press('right')  # 向右移动， 移动1秒，
        # dt.press('right')  # 向右移动， 移动1秒，

        time.sleep(1.5)  # 睡眠1.5秒

        dt.press('space')  # 单击空格操作
        time.sleep(0.5)  # 睡眠1.5秒gdf
        # aa1, bb1, cc1, dd1 = "挑战者", "#360", "师很", "#140"
        canshu = c.excelboot01(aa + 1)  # 调用excel表数据取值# 2p是加1 1p是加7
        n = 22
        if aa == 0:
            if pvp == 1:
                c.nvQiGong(n, 0.54, 0.26, 0, *canshu)  # 1p 气功师很烂丶

            else:

                c.nvQiGong(n, 0.54, 0.26, 0, *canshu)  # 2p 睡眠不足十
                # aa1, bb1, cc1, dd1 = "先驱者", "#422", "师很", "#140"
                # aa1, bb1, cc1, dd1="熟练者", "#410", "师很", "#140"
                # c.nvQiGong(n, 0.54, 0.26, 0)  # 气功师该加强了
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
            continue
        elif aa == 1:
            if pvp == 1:
                #
                # c.nvQiGong(n, 0.48, 0.2, 0)  # 1p 气功师很懒
                c.nvQiGong(n, 0.48, 0.2, 0, *canshu)  # 1p 气功师狠烂
            else:
                c.nvQiGong(n, 0.56, 0.26, 0, *canshu)  # 2p ll1ll数据i
                # c.nvQiGong(n, 0.48, 0.26, 0)  # 气功师该加强了
            time.sleep(3)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(390,500)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
            continue
        elif aa == 2:
            if pvp == 1:
                c.nvQiGong(n, 0.48, 0.2, 0,*canshu)# 1p 气功师很懒
                # c.nvQiGong(n, 0.62, 0.26, 0)  # 2p 睡眠不足丶
                #
            else:
                c.nvQiGong(n, 0.62, 0.3, 0, *canshu)  # 2p 睡眠不足丶
            time.sleep(3)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
            continue
        elif aa == 3:
            if pvp == 1:

                c.kuangzhanshi(n, 0.21, 0.23, 0,*canshu)  # 1p 狂战士
            else:
                # c.nvQiGong(n, 0.54, 0.32, 0)  # 气功师运气
                c.nvQiGong(n, 0.54, 0.2, 0, *canshu)  # 2p 十睡眠不足
                # c.zhaohuan(n, 0.05, 0.21, 0)  # 2p s睡眠不足s
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
            continue
        elif aa == 4:
            if pvp == 1:

                c.nanQiGong(n, 0,*canshu)  # 1p  男气功
            else:
                # c.nvQiGong(n, 0.54, 0.32, 0)  # 气功师运气
                # c.nvQiGong(n, 0.54, 0.2, 0, *canshu)  # 2p 十睡眠不足
                c.zhaohuan(n, 0.05, 0.21, 0, *canshu)  # 2p s睡眠不足s
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
            continue
        elif aa == 5:
            if pvp == 1:
                c.nanQiGong(n, 0)  # 1p  男气功
            else:
                # c.nvQiGong(n, 0.54, 0.32, 0)  # 气功师运气
                c.nvQiGong(n, 0.65, 0.2, 0, *canshu)  # 2p SS睡眠不足SS
                # c.zhaohuan(n, 0.05, 0.21, 0)  # 2p
            time.sleep(2)
            # x11, y11 = Caozuolei().left + 378,Caozuolei().top + 452,
            c.KeyPress1(27)  # 案件esc建
            # 425, 532 选人位置 424, 533
            time.sleep(3)
            # c.LeftClick(392,444)  # 单机鼠标左键
            c.LeftClick(399, 524)  # 单机鼠标左键
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
