import time

import pydirectinput  as dt
import win32gui

'''步骤1 获取当前【鼠标坐标】'''
# 获取当前鼠标【x y】坐标 309 118
'''
第1次 (185, 783) (135, 135, 0)
第2次 (125, 727) (72, 168, 16)
第3次 (149, 593) (80, 128, 255)

zz=((185, 783) ,(125, 727) ,(149, 593))
for i in range(1,4):
    time.sleep(5)
    point = win32api.GetCursorPos()
    # 获取某坐标的RGB颜色值  返回(236, 236, 236)
    rgb = pyautogui.screenshot().getpixel(zz[i])  # 手动填写 x y 坐标
    print('第{}次'.format(i),point,rgb)


获取某坐标的【RGB颜色值】

rgb = pyautogui.screenshot().getpixel((185, 783))  # 手动填写 x y 坐标
print(rgb)
# 获取某坐标的RGB颜色值  返回(236, 236, 236)

'''

'''
keyboard.tap_key('H') 						# 点击H键
keyboard.tap_key('H', n=2, interval=5) 		# 点击H键2次，每次间隔5秒
keyboard.tap_key(keyboard.numpad_keys[5])   # 点击小键盘5
# 通过坐标获取坐标下的【窗口句柄】
keyboard.tap_key(keyboard.function_keys[5]) # 点击功能键F5
'''
# time.sleep(5)
# point = win32api.GetCursorPos()
# print(point)
# 如果函数运行期间想要停止，请把鼠标移动到屏幕得左上角（0，0）位置，
# 这触发pyautogui.FaailSafeException异常，从而终止程序运行。
dt.FAILSAFE = True  # 默认True则鼠标(0,0)可触发异常；False不触发

hwnd = win32gui.WindowFromPoint((308, 444))  # 请填写 x 和 y 坐标
print(hwnd)
time.sleep(1)
# 通过句柄将窗口放到最前
# win32gui.SetForegroundWindow("句柄值")
# dpyautogui.press('alt')
win32gui.SetForegroundWindow(hwnd)
time.sleep(5)

for i in range(1, 3):
    time.sleep(0.2)
    for j in range(1, 5):
        # print('right开始按下{}次'.format(j))
        if j == 1:
            time.sleep(0.15)  # 按下两秒
            dt.press('f')
            time.sleep(1)  # 按下两秒
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.2)
            dt.keyUp('right')  # ：模拟按键松开按键
            time.sleep(0.05)
            # 2.8 = 1.6+1.2
            dt.press('d')
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.2)
            dt.keyUp('right')  # ：模拟按键松开按键
            time.sleep(0.05)
        elif j == 2:
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(0.6)
            dt.keyUp('right')  # ：模拟按键松开按键
            dt.press('g')
            time.sleep(3)

        elif j == 3:
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.95)
            dt.keyUp('right')  # ：模拟按键松开按键
            time.sleep(1)
            dt.press('f')
            time.sleep(0.45)
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1)
            dt.keyUp('right')  # ：模拟按键松开按键
            time.sleep(3)
            dt.press('9')
            time.sleep(2)
            dt.press('right')
            time.sleep(0.0075)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.8)
            dt.keyUp('right')  # ：模拟按键松开按键
        elif j == 4:  # 奇数 反之偶数
            dt.press('right')
            time.sleep(0.013)  # 按下两秒
            dt.keyDown('right')  # ：模拟按键按下
            time.sleep(1.7)  # 按下19秒
            dt.keyUp('right')  # ：模拟按键松开按键
            time.sleep(0.013)  # 按下两秒
            dt.press('up')
            time.sleep(0.45)  # 按下两秒
            dt.press('g')
            time.sleep(0.45)  # 按下两秒
            dt.press('ctrl')
            time.sleep(0.45)  # 按下两秒
            dt.press('d')
            time.sleep(0.45)  # 按下两秒
            dt.press('f')
            time.sleep(7.50)  # 按下两秒
            dt.press('g')
            time.sleep(10)  # 按下两秒
            dt.press('0')
            time.sleep(1)  # 按下两秒
            for ii in range(1, 4):
                if i == 12:
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
                    pass
                    continue
            time.sleep(5)  # 按下两秒

            # print('0')
            # print(i)

            time.sleep(2)

            if i == 25:
                dt.press('f12')
            else:
                dt.press('f10')
            time.sleep(5)
            # print('方法5运行{}'.format(j))

        time.sleep(0.5)
        # print('大循环{}'.format(j))
    sss = i * 8
    if i == 25:
        # os.system("shutdown -s -t 30")
        break

    print('费了{}疲劳'.format(sss))
'''
dt.keyDown('a')#：模拟按键按下
time.sleep(2) #按下两秒0
dt.keyUp('a') #：模拟按键松开time.sleep(2)
'''
# print('pass3')
# win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
