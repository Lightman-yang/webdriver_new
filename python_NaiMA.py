import os
import time

import pydirectinput as dt
import win32gui


class DXC_NaiMA():
    def DXCNaiMA(self, DXCNaiMAx, DXCNaiMAy, num_parameter2, Restart_computer_parameter2):
        '''步骤1 获取当前【鼠标坐标】'''
        # 获取当前鼠标【x y】坐标 309 118

        # time.sleep(5)
        # point = win32api.GetCursorPos()
        # print(point)
        # 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
        # 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
        dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发

        hwnd = win32gui.WindowFromPoint((DXCNaiMAx, DXCNaiMAy))  # 请填写 x 和 y 坐标
        print(hwnd)
        time.sleep(1)
        # 通过句柄将窗口放到最前
        # win32gui.SetForegroundWindow("句柄值")
        # dpyautogui.press('alt')
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(5)

        for i in range(1, 60):
            num = num_parameter2  # num不能是奇数 运行几次
            # move_seep = -0.277  # 57.7
            # m_button = 'h'
            # print(move_seep)
            Restart_computer = Restart_computer_parameter2  # Restart_computer为0或者1，0关闭电脑，1不关闭电脑

            for j in range(1, 7):

                # print('right开始按下{}次'.format(j))
                if j == 2:
                    # dt.press('e')
                    # time.sleep(1)  # 按下两秒
                    # dt.press('right')
                    # time.sleep(0.0075)  # 按下两秒
                    dt.press('w')
                    time.sleep(0.155)
                    dt.press('g')
                    time.sleep(0.155)
                    dt.press('f')
                    time.sleep(5.5)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.6)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 1:
                    dt.press('y')
                    time.sleep(1)
                    # dt.press('right')
                    # time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.3)
                    dt.keyUp('right')  # ：模拟按键松开按键
                elif j == 3:
                    time.sleep(0.03)
                    dt.press('t')
                    time.sleep(0.0075)  # 按下两秒
                    dt.keyDown('right')  # ：模拟按键按下

                    time.sleep(2.75)
                    dt.press('w')
                    time.sleep(0.155)
                    dt.press('f')
                    time.sleep(0.2)
                    dt.keyUp('right')  # ：模拟按键松开按键

                elif j == 4:

                    time.sleep(0.015)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(2.4)  # 按下两秒
                    dt.keyUp('right')  # ：模拟按键松开按键
                    # dt.press('e')

                elif j == 5:
                    dt.press('w')
                    time.sleep(0.155)
                    dt.press('g')
                    time.sleep(1.5)
                    dt.press('9')
                    time.sleep(2.3)
                    from python_findpicture import Caozuolei1
                    if Caozuolei1().matchingParameter() == 1:

                        dt.keyDown('down')  # ：模拟按键按下
                        time.sleep(0.1)  # 按下两秒
                        dt.keyUp('down')  # ：模拟按键松开按键
                        time.sleep(0.0075)  # 按下两秒

                        dt.keyDown('right')  # ：模拟按键按下
                        time.sleep(1.9)
                        dt.keyUp('right')  # ：模拟按键松开按键

                        # time.sleep(10000)                    #测试
                        time.sleep(0.0075)  # 按下两秒
                        dt.keyDown('up')  # ：模拟按键按下
                        time.sleep(0.1)  # 按下两秒
                        dt.keyUp('up')  # ：模拟按键松开按键
                        time.sleep(2)  # 按下两秒

                    else:
                        time.sleep(0.02)
                        dt.keyDown('right')  # ：模拟按键按下
                        time.sleep(1.9)
                        dt.keyUp('right')  # ：模拟按键松开按键


                elif j == 6:  # 奇数 反之偶数
                    time.sleep(3)
                    dt.keyDown('right')  # ：模拟按键按下
                    time.sleep(0.5)  # 按下19秒
                    dt.keyUp('right')  # ：模拟按键松开按键
                    dt.press('w')
                    time.sleep(0.05)  # 按下19秒
                    dt.press('x')
                    time.sleep(0.05)  # 按下19秒
                    dt.press('t')  # 像上按一下
                    time.sleep(0.3)
                    dt.press('d')
                    time.sleep(0.3)
                    dt.press('f')
                    time.sleep(0.013)  # 按下两秒
                    time.sleep(6)  # 按下两秒
                    for z in range(1, 3):
                        time.sleep(0.5)  # 按下两秒
                        # dt.press('down')  # 像下按一下
                        dt.press('a')
                    time.sleep(1)  # 按下两秒
                    dt.press('0')
                    time.sleep(3)  # 按下两秒
                    for ii in range(1, 4):
                        num_num = num / 2
                        if i == num_num or i == 20 or i == num:
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
                    time.sleep(2)
                    if i == num:
                        dt.press('f12')
                    else:
                        dt.press('f10')

                    time.sleep(4)
                    # print('方法5运行{}'.format(j))

                time.sleep(0.5)
                # print('大循环{}'.format(j))
            sss = i * 8
            if i == num and Restart_computer == 0:
                # os.system("shutdown -s -t 30")
                break
            elif i == num and Restart_computer == 1:
                os.system("shutdown -s -t 30")  # 30秒关闭电脑
                break
            print('费了{}疲劳'.format(sss))
        '''
        dt.keyDown('a')#：模拟按键按下
        time.sleep(2) #按下两秒0
        dt.keyUp('a') #：模拟按键松开time.sleep(2)
        '''
        # print('pass3')
        # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)

# if __name__ == '__main__':
#     DXC_NaiMA().DXCNaiMA(309, 118, 20, 0)
