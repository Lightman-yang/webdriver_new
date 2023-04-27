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
time.sleep(2)


def movingFigur_Down(time_sleep):
    time.sleep(0.15)  # 按下两秒
    dt.keyDown('down')  # 向下移动
    time.sleep(time_sleep)  # 按下两秒
    dt.keyUp('down')  # ：模拟按键松开


# 方法为像右移动
def movingFigur_right(time_sleep):
    time.sleep(0.15)  # 像右移动
    dt.keyDown('right')  # 像右移动
    time.sleep(time_sleep)  # 像右移动
    dt.keyUp('right')  # ：模拟按键松开右


# 方法为像上移动
def movingFigur_up(time_sleep):
    time.sleep(0.15)  # 像右移动
    dt.keyDown('up')  # 像右移动
    time.sleep(time_sleep)  # 像右移动
    dt.keyUp('up')  # ：模拟按键松开右


# 方法为像左移动
def movingFigur_left(time_sleep):
    time.sleep(0.15)  # 像左移动
    dt.keyDown('left')  # 像左移动
    time.sleep(time_sleep)  # 像左移动
    dt.keyUp('left')  # ：模拟按键松开左


def sleep_1000():
    while dt.press('+'):
        time.sleep(1000)
    else:
        dt.press('num9')


if __name__ == '__main__':
    time.sleep(5)
    movingFigur_Down(0.95)  # 向下移动，移动一秒

    time.sleep(0.5)  # 睡眠0.5秒

    movingFigur_right(9)  # 向右移动， 移动8秒，

    movingFigur_up(0.15)  # 向上移动， 移动0.15秒，

    time.sleep(1.5)  # 睡眠1.5秒
    for i in range(10):
        time.sleep(0.75)  # 睡眠1.5秒
        dt.press('left')  # 向上移动， 移动0.15秒，

    time.sleep(0.5)  # 睡眠1.5秒

    dt.press('right')  # 向右移动， 移动1秒，

    time.sleep(3)  # 睡眠1.5秒

    dt.press('space')  # 单击空格操作
    time.sleep(3)  # 睡眠1.5秒
    from python_v2023nvqigong import nvqigong

    nvqigong.NvQiGong(308, 444)

'''
dt.keyDown('a')#：模拟按键按下
time.sleep(2) #按下两秒0
dt.keyUp('a') #：模拟按键松开time.sleep(2)
'''

# print('pass3')
# win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
