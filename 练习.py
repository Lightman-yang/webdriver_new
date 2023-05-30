# b = "子"
# a = '{}曰：学而实习之，不亦说乎；{}又曰：友朋自远方来，不亦君子呼！{}'.format(b, b, b)
#
# print(a)
# print('%s曰：学而实习之，不亦说乎；%s又曰：友朋自远方来，不亦君子呼！%s' % (b, b, b))
#
# print()

# a=os.system('dir')
# print(a)
# b=os.system('mkdir zzz')
# print(b)
#
# a=os.system('dir')
# print(a)
from time import sleep  # 导入时间休眠函数

xxyy = [1, 2, 3, 4]
xxyy1 = []

import os
import time
from random import uniform

import pydirectinput  as dt
import win32gui
from comtypes.client import CreateObject
from win32gui import FindWindow


class Caozuolei1():
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
            # lw的移动不准确！采用pydirectinput库
            # dt.moveTo((self.lw.x()+55),(self.lw.y()+124))
            # self.lw.MoveTo((self.lw.x()+55),(self.lw.y()+124))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55), '+', "纵向坐标为：", '+', (self.lw.y() + 124), '+ ', "序号为：",
                  '+',
                  self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            x = self.lw.x() + 55
            y = self.lw.y() + 124
            return x, y
        else:
            print("没有！")
            return 1500, 1500

    def Find_Pic1(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                  chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:
            # dt.moveTo((self.lw.x()+55+45),(self.lw.y()+124+84))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55 + 45), '+', "纵向坐标为：", '+', (self.lw.y() + 124 + 84), '+ ',
                  "序号为：", '+', self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            x = self.lw.x() + 55 + 45
            y = self.lw.y() + 124 + 84
            return x, y
        else:
            print("没有！")
            return 1500, 1500

    def Find_Pic2(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                  chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:
            # dt.moveTo((self.lw.x()+55+45),(self.lw.y()+124+84))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55 + 45), '+', "纵向坐标为：", '+', (self.lw.y() + 124 + 84), '+ ',
                  "序号为：", '+', self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            x = self.lw.x() + 55 + 155
            y = self.lw.y() + 124 + 110
            return x, y
        else:
            print("没有！")
            return 1500, 1500

    def Find_PicX(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                  chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:
            # dt.moveTo((self.lw.x()+55+45),(self.lw.y()+124+84))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55 + 45), '+', "纵向坐标为：", '+', (self.lw.y() + 124 + 84), '+ ',
                  "序号为：", '+', self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            x = self.lw.x() + 48
            y = self.lw.y() + 80
            return x, y
        else:
            print("没有！")
            return 1500, 1500

    def Find_PicX1(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                   chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:
            # dt.moveTo((self.lw.x()+55+45),(self.lw.y()+124+84))
            print("找到图片, 横向坐标为：", '+', (self.lw.x() + 55 + 45), '+', "纵向坐标为：", '+', (self.lw.y() + 124 + 84), '+ ',
                  "序号为：", '+', self.lw.idx())
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            x = self.lw.x() + 110
            y = self.lw.y()  # + 80
            return x, y
        else:
            print("没有！")
            return 1500, 1500

    def Set_Dict(self, index, file):

        ret = self.lw.SetDict(index, file)
        if ret == 1:
            print("自库设置成功！")
        else:
            print("自库设置失败！")

    # 找字返回坐标方法
    def Find_Str(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor):

        ret = self.lw.FindStr(x1, y1, x2, y2, string, color_format, sim, isbackcolor)

        if ret == 1:
            self.lw.MoveTO(self.lw.x(), self.lw.y())
            print("找到字符, 横向坐标为：", '+', (self.lw.x()), '+', "纵向坐标为：", '+', (self.lw.y()))
            # print("找到图片, 横向坐标为："+self.lw.x() + "纵向坐标为：" + self.lw.y() + "序号为：" + self.lw.idx())
            self.lw.LeftClick()
            print("点击左键进入，大乱斗")
        else:
            print("没有字符！")
            return 0

    def Find_Strkspp(self):  # 获取"开始匹配"字符串
        print("字符匹配中")
        for i in range(1, 10):

            aa = Caozuolei1().Find_Str(
                x1=0,
                y1=0,
                x2=1000,
                y2=1000,
                string='开始匹配',
                color_format="#105",
                sim=0.95,
                isbackcolor=0)
            if aa is not None:
                return aa
            else:
                pass

    # sleep(random.randint(0, 2))  # 随机睡眠一个小会儿

    # 找字功能
    def Find_Ocr(self, x1, y1, x2, y2, color_format, sim, linesign, isbackcolor):
        ret = self.lw.Ocr(x1, y1, x2, y2, color_format, sim, linesign, isbackcolor)
        if ret is not None:
            # print(ret)
            return ret
        else:
            # print(0)
            return '非'

    def selfxy(self):  # 获取人物坐标
        print("人物坐标")
        for i in range(1, 10):

            aa = Caozuolei1().Find_Pic1(
                x1=70,
                y1=100,
                x2=800,
                y2=1000,
                pic_name='先驱者100_1b1615.bmp' + '|' + '先驱者200_47a70f.bmp' + '|' + '先驱者300_47a70f.bmp',
                delta_color='1b1615' + '|' + '47a70f' + '47a70f',
                sim=0.95,
                dir=3,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None:
                return aa
            else:
                pass

    # sleep(random.randint(0, 2))  # 随机睡眠一个小会儿

    def money_xy(self):  # 获取金币坐标
        print('金币坐标')
        for i in range(1, 10):
            aa = Caozuolei1().Find_Pic(
                x1=60,
                y1=100,
                x2=800,
                y2=800,
                pic_name='jinbi222.bmp',
                delta_color='1b1615',
                sim=0.98,
                dir=3,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None and (aa[0] != 1500 and aa[1] != 1500):
                return aa
            else:
                pass

                # 1b1615
                # sleep(random.randint(0, 2))  # 随机睡眠一个小会儿

    def sellGoods_xy(self):  # 一键出售A 菜单
        print('一键出售A 菜单坐标')
        for i in range(1, 10):
            aa = Caozuolei1().Find_Pic1(
                x1=0,
                y1=0,
                x2=600,
                y2=800,
                pic_name='一键出售_1b1615.bmp',
                delta_color='1b1615',
                sim=0.99,
                dir=0,
                timeout=0,
                ischick=1,
                chickdex=29,
                chickdey=20,
                chickdely=100)
            if aa is not None and (aa[0] != 1500 and aa[1] != 1500):
                return aa
            else:
                pass

    def door_xy(self):  # 获取普通门坐标
        print('普通门')
        for i in range(1, 10):
            aa = Caozuolei1().Find_Pic(
                x1=200,
                y1=200,
                x2=1000,
                y2=1000,
                pic_name='门1.bmp',
                delta_color='1b1615',
                sim=0.45,
                dir=3,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None and (aa[0] != 1500 and aa[1] != 1500):
                print("找到了{}".format(aa))
                return aa
            else:
                print('没找到门')
                pass

    def spaceTimeBossDoor_xy(self):  # 获取时空传送boss门坐标
        print('获取时空传送boss门坐标')
        for i in range(1, 10):
            aa = Caozuolei1().Find_Pic2(
                x1=100,
                y1=100,
                x2=1000,
                y2=1000,
                pic_name='时空门传送门图_47a70f.bmp',
                delta_color='47a70f',
                sim=0.66,
                dir=1,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None and (aa[0] != 1500 and aa[1] != 1500):
                print("找到了{}".format(aa), type(aa))
                return aa
            else:
                print('没找到门')

    def spaceTimeBossDoor_xy1(self):  # 获取时空传送boss门小图标坐标
        print('获取时空传送boss门小图标坐标')
        for i in range(1, 10):
            aa = Caozuolei1().Find_PicX(
                x1=40,
                y1=40,
                x2=300,
                y2=300,
                pic_name='时空门22_47a70f.bmp',
                delta_color='47a70f',
                sim=0.89,
                dir=1,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None and aa != (1500, 1500):
                print("找到了{}".format(aa))
                return aa
            else:
                print('没找时空传送boss门小图标坐标')

    def arm_xy1(self):  # 获取武器装备坐标
        print('获取武器装备坐标')
        for i in range(1, 20):
            aa = Caozuolei1().Find_PicX1(
                x1=50,
                y1=300,
                x2=800,
                y2=800,
                pic_name='FND2_47a70f.bmp',
                delta_color='47a70f',
                sim=0.90,
                dir=1,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None and aa != (1500, 1500):
                print("找到了{}武器装备坐标".format(aa))
                return aa
            else:
                print('没找武器装备坐标！')

        # 1b1615
        # sleep(random.randint(0, 2))  # 随机睡眠一个小会儿

    def doorboss_xy(self):  # 获取boss坐标
        print('boss门')
        for i in range(1, 10):
            aa = Caozuolei1().Find_Pic2(
                x1=200,
                y1=200,
                x2=1000,
                y2=1000,
                pic_name='BOSS门_1b1615.bmp' + '|' + 'BOSS门2_1b1615.bmp',
                delta_color='1b1615' + '|' + '1b1615',
                sim=0.66,
                dir=3,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if aa is not None:
                print("找到了boss门{}".format(aa))
                return aa
            else:
                print('没找到boss门')
                pass

    def key_movemove(self, shijian, key_keyboard):
        dt.keyDown('{}'.format(key_keyboard))  # ：模拟按键按下
        time.sleep(shijian)  # 按下19秒
        dt.keyUp('{}'.format(key_keyboard))  # ：模拟按键松开按键

    def movemovemove(self, aa, bb):
        import pydirectinput  as dt
        a = aa[1]  # 人物坐标
        print(a, type(a))
        b = bb  # 其他坐标
        print(a - b, abs(a - b))

        for i in range(1, 100):
            if (abs(a - b)) > 10:
                ax, ay = Caozuolei1().selfxy()
                print(a, "人物坐标Y")
                print(type(a))
                if ay == 1500:
                    continue
                elif ay > b and (ay - b) < 50 and (ay - b) >= 10:
                    dt.press('up')
                elif ay > b and (ay - b) >= 50:
                    time.sleep(1)
                    c = (ay - b) * 0.0001 + 0.2
                    Caozuolei1().key_movemove(c, 'up')
                elif b > ay and (b - ay) >= 50:
                    time.sleep(1)
                    c = (b - ay) * 0.0001 + 0.2
                    Caozuolei1().key_movemove(c, 'down')
                elif b > a and 50 > (b - ay) >= 10:
                    time.sleep(1)
                    dt.press('down')
                else:

                    print('没找到')
                    print(Caozuolei1().selfxy())
                    break

    def movemovemoveheng(self, aa, bb):
        import pydirectinput  as dt
        a = aa[0]  # 人物坐标
        b = bb  # 其他坐标
        print(a - b, abs(a - b))
        for i in range(1, 100):
            if (abs(a - b)) > 10:
                print(a - b)

                a, ay = Caozuolei1().selfxy()
                print(a, "人物坐标X")
                if a == 1500:
                    continue
                elif a > b and (a - b) < 50 and (a - b) >= 10:
                    time.sleep(1.5)
                    dt.press('left')
                elif a > b and (a - b) >= 50:
                    time.sleep(1.5)
                    c = (a - b) * 0.0001 + 0.2
                    Caozuolei1().key_movemove(c, 'left')
                elif b > a and (b - a) >= 50:
                    time.sleep(1.5)
                    c = (b - a) * 0.0001 + 0.2
                    Caozuolei1().key_movemove(c, 'right')
                elif b > a and 50 > (b - a) >= 10:
                    dt.press('right')
                else:
                    print('没找到')
                    print(Caozuolei1().selfxy())
                    break
            else:
                print("移动到当前位置")

    def matchingParameter(self):

        for i in range(1, 10):

            if (Caozuolei1().spaceTimeBossDoor_xy1() is not None) or (
                    Caozuolei1().spaceTimeBossDoor_xy() is not None):
                print('匹配成功！')
                return 1
            else:
                print('不匹配！')
                return 0

    def Find_Pic55(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                   chickdely):
        ret = self.lw.findpic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, timeout, ischick, chickdex, chickdey,
                              chickdely)

        if ret == 1:
            x = self.lw.x()
            y = self.lw.y()

            return x, y
        else:
            print("没有！")
            return 0

    def Find_Picdoor(self):
        for i in range(1, 10000):
            time.sleep(0.4)
            z = self.Find_Pic55(
                x1=0,
                y1=0,
                x2=1000,
                y2=1000,
                pic_name="门_47a70f.bmp",
                delta_color="47a70f",
                sim=0.7,
                dir=0,
                timeout=0,
                ischick=0,
                chickdex=0,
                chickdey=0,
                chickdely=0)
            if z != 0:
                x = z[0]
                y = z[1]
                xxyy[-2:] = x, y
                print("Find_Picdoor=", xxyy)
            else:
                xxyy[-2:] = 0, 0
                print("Find_Picdoor=", xxyy)

    def FindStr(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor):
        ret = self.lw.FindStr(x1, y1, x2, y2, string, color_format, sim, isbackcolor)
        if ret == 1:
            return self.lw.x(), self.lw.y()
        else:
            return 0

    def FindStrex(self, x1, y1, x2, y2, string, color_format, sim, isbackcolor):  # 找字返回坐标集合
        ret = self.lw.FindStrEx(x1, y1, x2, y2, string, color_format, sim, isbackcolor)
        if ret != None:

            ret1 = ret.split('|')
            # print(ret1)
            # sss=ret1.strip() #去掉前后字符串中的特殊字符'’'
            # ret1N=[]
            # for i in range(len(ret1)):
            #     array1 = ret1[i].split(',')
            #     ret1N.append(array1)
            #     for i in range(len(ret1N)):
            #         if int(ret1N[i][1]) > 300:
            #             print(ret1N[i])
            #             x=int(ret1N[i][1])
            #             y=int(ret1N[i][2])
            #             return x, y
            #     else:
            #         return
            # print(ret1)
            return ret1

            # print('ret1=',ret2,'r=',ret1,type(ret))
            # time.sleep(222222)

        else:
            # print(0000)
            print("失败了吗")
            return None

    def Find_Strexxy(self):  # 其它坐标 多个坐标
        for i in range(1, 100000):

            sleep(1)
            z = self.FindStrex(
                x1=0,
                y1=0,
                x2=1200,
                y2=1200,
                string="开洞",
                color_format="#380",
                sim=0.8,
                isbackcolor=0)
            # print(z)
            if z != None:
                #
                # ret1=z.strip() #去掉前后字符串中的特殊字符'’'
                # print(z,"test")
                # print(z)
                # print(z[1],type(z[1]))
                ret1N = []
                for x in z:  # 第一个for循环是在list中
                    for y in x.split(','):  # split只能在str上 所有再次for循环
                        ret1N.append(y)
                # print(ret1N,'?1')
                for i in range(2, len(ret1N))[::3]:  # 跨度三个下标，从元素下标2开始取
                    # print(ret1N[i],ret1N[i-1],"?在哪")
                    if (int(ret1N[i - 1])) > 300:  # 判断是否X坐标大于300，大于就用，
                        # print(ret1N[i - 1], ret1N[i],'?')

                        xxyy[-2:] = int(ret1N[i - 1]), int(ret1N[i])
                        print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]), ',?')
                        # print(xxyy)
                        break
                        # elif (int(ret1N[i-1])) < 300:
                        #      print(ret1N[i-1])
                        #      xxyy[-2:] = 3, 4
                        #      return

            else:
                xxyy[-2:] = 2, 2
                # print('x={},y={}'.format(0, 0))
                continue

                # x = z[0]
                # y = z[1]
                # xxyy1= x, y
                # print('x={},y={}'.format(x, y))

                # xxyy = 0, 0

    def Find_srt(self, usr_string1, usr_color_format1, usr_string2, usr_color_format2):  # 人物坐标
        for i in range(1, 2):

            sleep(1)
            z = self.FindStr(
                x1=0,
                y1=0,
                x2=1000,
                y2=1000,
                string=usr_string1,  # "先驱者",  # "挑战者"
                color_format=usr_color_format1,  # "#422",  ##380
                sim=0.75,
                isbackcolor=0)
            print(z)
            if z != 0:
                x = z[0] + 68
                y = z[1] + 135
                xxyy[0:2] = x, y
                print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1],xxyy[2],xxyy[3]))
            else:
                for j in range(0, 1):
                    sleep(1)
                    z = self.FindStr(
                        x1=0,
                        y1=0,
                        x2=1000,
                        y2=1000,
                        string=usr_string2,  # "不足",
                        color_format=usr_color_format2,  # "#422",
                        sim=0.8,
                        isbackcolor=0)
                    if z != 0:
                        x = z[0]
                        y = z[1] + 131

                        xxyy[0:2] = x, y
                        print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]), ',?')
                    else:
                        pass
                        # print(0, xxyy)
                        #
                        # print("从新找")
                        # continue

    def Find_srt1(self):  # 其它坐标
        for i in range(1, 100000):

            sleep(1)
            z = self.FindStr(
                x1=0,
                y1=0,
                x2=1000,
                y2=1000,
                string="开洞",
                color_format="#380",
                sim=0.50,
                isbackcolor=0)
            # print(z)
            if z != 0:
                x = z[0]
                y = z[1]
                xxyy[-2:] = x, y
                print('x={},y={}'.format(x, y))
                break
            else:

                xxyy[-2:] = 0, 0
                print('x={},y={}'.format(0, 0))
                break

    def movemovemoveheng1(self):
        import pydirectinput  as dt

        # a = aa  # 人物坐标
        # b = bb  # 其他坐标
        # print(a - b, abs(a - b),"进来了")
        for i in range(1, 10):
            a = xxyy[0]  # 人物坐标
            b = xxyy[2]  # 其他坐标
            if (abs(a - b)) > 10:
                print(abs(a - b))
                # a, b = xxyy[0],xxyy[2]
                print(a, b, "人物坐标X")
                time.sleep(1)
                if b == 0 or b < abs(5):
                    print(b, '小于5，直接退出了')
                    return

                elif a > b and (10 <= (a - b) < 50 and (a - b)):
                    time.sleep(0.5)
                    dt.press('left')
                    break
                elif a > b and (a - b) >= 50:
                    time.sleep(0.5)
                    c = (a - b) * 0.0001 + 0.2
                    Caozuolei1().key_movemove(c, 'left')
                elif b > a and (b - a) >= 50:
                    time.sleep(0.5)
                    c = (b - a) * 0.002 + 0.2
                    Caozuolei1().key_movemove(c, 'right')
                elif b > a and 50 > (b - a) >= 10:
                    dt.press('right')
                    break

            else:
                print("移动到当前位置")
                break

    def movemovemove2(self):  # Y轴移动
        import pydirectinput  as dt
        # a = aa  # 人物坐标
        # b = bb  # 其他坐标
        # print(a - b, abs(a - b))

        for i in range(1, 10):
            a = xxyy[1]  # 人物坐标
            b = xxyy[3]  # 其他坐标
            if (abs(a - b)) > 10:
                print(a - b)
                a, b = xxyy[1], xxyy[3]
                print('人物坐标{},{},门坐标{},{}'.format(xxyy[0], xxyy[1], xxyy[2], xxyy[3]))
                print(a, b, "人物坐标y")
                time.sleep(1)
                if b == 0 or abs(b) < 5:
                    return
                elif a > b and (a - b) < 50 and (a - b) >= 10:
                    dt.press('up')
                    continue
                elif a > b and (a - b) >= 50:
                    time.sleep(0.5)
                    c = (a - b) * 0.001 + 0.3
                    Caozuolei1().key_movemove(c, 'up')
                    continue
                elif b > a and (b - a) >= 50:
                    time.sleep(0.5)
                    c = (b - a) * 0.002 + 0.3
                    Caozuolei1().key_movemove(c, 'down')
                    continue
                elif b > a and 50 > (b - a) >= 10:
                    time.sleep(0.5)
                    dt.press('down')
                    return
            else:

                print('没找到,或者已经结束')

                return


#
if __name__ == '__main__':
    time.sleep(2)
    import pydirectinput  as dt

    c = Caozuolei1()
    c.lw.MoveWindow(c.hwnd, 0, 0, 0, 0)  # 移动窗口，抢两个零是xy，后两个是窗口高度和宽度，默认为0不生效
    c.Set_Dict(0, 'test3.txt')
    # c.Find_srt()c
    # c.Find_Picdoor()
    # c.Find_Strexxy()
    for i in range(1, 20):
        c.Find_srt("熟练者", "#422", "功师", "#422")
        print(int(xxyy[0]), (int(xxyy[0]) - 606))

        if (int(xxyy[0]) - 606) < -10:
            print((int(xxyy[0]) - 606), 'x')
            dt.press('right')
        elif (int(xxyy[0]) - 606) > 10:
            print((int(xxyy[0]) - 606), 'x')
            dt.press('left')
        elif 11 < (int(xxyy[0]) - 606) > -11:
            print((int(xxyy[0]) - 606), 'x')
            continue
        elif (int(xxyy[1]) - 449) < -10:
            print((int(xxyy[1]) - 449), 'y')
            dt.press('down')
        elif (int(xxyy[1]) - 449) > 10:
            print((int(xxyy[1]) - 449), 'y')
            dt.press('up')
        elif 11 < (int(xxyy[1]) - 449) > -11:
            print((int(xxyy[1]) - 449), 'y')
            continue
        elif 11 < (int(xxyy[0]) - 606) > -11 and 11 < (int(xxyy[1]) - 449) > -11:
            print((int(xxyy[1]) - 449), 'y')
            break
        else:

            print((int(xxyy[1]) - 449), 'y', (int(xxyy[0]) - 606), 'x')
            break

    # zzz = Thread(target=c.Find_Strexxy)  #606 449 596 442
    # ZZZ = Thread(target=c.Find_srt("先驱者","#422","不足","#422"))
    # ZZZ = Thread(target=c.Find_srt("熟6者", "#422", "功师", "#422"))
    # zzz.start()
    # ZZZ.start()
    # # a = xxyy[0]  # 人物坐标
    # # b = xxyy[-2]  # 其他坐标
    # print("测试")
    # time.sleep(10)
    # print(xxyy, xxyy[0], xxyy[-2], xxyy[1], xxyy[-1])
    # for i in range(1, 250):
    #     if i > 1:
    #         c.movemovemoveheng1()
    #         c.movemovemove2()

    #         y1=0,
    #         x2=1200,
    #         y2=1200,
    #         color_format="#360",
    #         sim=0.95,
    #         linesign="五陵",
    #         isbackcolor=0)
    #     for i in range (1,170):
    #         print(i)
    #         if  c.Find_Str(
    #                 x1=0,
    #                 y1=0,
    #                 x2=1000,
    #                 y2=1000,
    #             string='开始匹配',
    #                 color_format="#105",
    #                 sim=0.9,
    #                 isbackcolor=0) ==0:
    #             dt.moveTo(500,500)
    #             for z in range(1,21):
    #
    #                 dt.press('c')
    #                 for j in range(1,8):
    #                     time.sleep(0.075)
    #                     dt.press('x')  # ：模拟按键按下
    #                 dt.press('left')
    #                 for h in range(1, 8):
    #                     time.sleep(0.5)
    #                     dt.press('x')  # ：模拟按键按下
    #                 time.sleep(1)
    #                 dt.press('s')
    #                 print('i==', z)
    #         else:
    #             pass

    #     # dt.moveTo(c.arm_xy1()[0],c.arm_xy1()[1],duration=3)
    #     # time.sleep(2)
    #     # dt.moveTo(238,568,duration=3)
    #
    #     #c.spaceTimeBossDoor_xy()
    #     #c.spaceTimeBossDoor_xy1()
    #     #print(c.door_xy()[0],c.door_xy()[1])
    #     i=1
    #     while i<2:
    #           time.sleep(2)
    #           c.selfxy()
    #           bx,by=c.arm_xy1()
    #           if bx == 1500 or by == 1500:
    #               print('没值，1500')
    #           else:
    #               c.movemovemove(c.selfxy(), by)
    #               c.movemovemoveheng(c.selfxy(), bx)
    #           i+=1
    #           print(i)
    #     '''
    #     #dt.moveTo()
    #     #c.selfxy()
    #     # c.money_xy()
    #     # time.sleep(1000)
    #     bx,by=c.arm_xy1()
    #     if bx==1500 or by ==1500:
    #         print('没值，1500')
    #     else:
    #         c.movemovemove(c.selfxy(), by)
    #         c.movemovemoveheng(c.selfxy(), bx)
    #     #dt.press('up')
    #     #print(type(c.selfxy()),c.selfxy())
    #
    #     #c.key_movemove(0.11,'up')
    #     time.sleep(3)
    #     '''
    # #     #c.selfxy()
    #     print(os.times())
    c.UnBind()  # 解除绑定
