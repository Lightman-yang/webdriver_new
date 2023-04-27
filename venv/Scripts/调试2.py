# _*_ coding: UTF-8 _*_
import psutil
import pydirectinput  as Qt
import win32api
import win32gui
import pyautogui as QQgui
# 找到了 Point(x=224, y=295)  1381, 326
import time

import win32process
# 找到了 Point(x=224, y=295)  1381, 326
import time

import psutil
import pyautogui as QQgui
import pydirectinput  as Qt
import win32api
import win32gui
import win32process

QQgui.FAILSAFE = True

# 获取当前鼠标【x y】坐标
time.sleep(5)
point = win32api.GetCursorPos()
x1, y1 = point
print(point)
time.sleep(3)
hwnd = win32gui.WindowFromPoint((point))  # 请填写 x 和 y 坐标
print(hwnd)
# (400,313),(403,641)   (964, 230)

time.sleep(1)
# 通过句柄将窗口放到最前
# win32gui.SetForegroundWindow("句柄值")
# dpyautogui.press('alt')
win32gui.SetForegroundWindow(hwnd)
time.sleep(1)
Qt.PAUSE = 2.5
'''步骤3 通过窗口句柄获取 【线程ID（hread_id）, 和 进程ID（process_id）】'''
# 通过句柄获取【线程ID 进程ID】
# hread_id, process_id = win32process.GetWindowThreadProcessId('句柄值')
hread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
print(hread_id, process_id)

'''步骤5 通过进程ID 获取【标准路径】'''
# 通过进程ID 获取主文件程序【标准路径】 列：D:/filed/windoee/weixin.exe
# p_bin = psutil.Process('进程ID').exe()
p_bin = psutil.Process(process_id)
print(p_bin)

'''步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置'''
# 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
# left, top, right, bottom = win32gui.GetWindowRect('句柄值')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)
x11, y11 = left + 378, top + 452,
print('点击坐标', x11, y11, '游戏坐标', left, top, right, bottom, '鼠标停放位置', point)
x22, y22 = left + 249, top + 249,
print('选择人物点击坐标', x22, y22, '游戏坐标', left, top, right, bottom, '鼠标停放位置', point)
# F:\Program Files (x86)\WeGameApps\地下城与勇士\DNF.exe
# app = pywinauto.Application().connect(path='your_process_name.exe')
# app.MainDialog.click_input(coords=(x, y))

print('测试')

# def MP(x,y):#Move Postion
#     try:
#         x=int(x)
#         y=int(y)
#         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
#         print("pass")
#     except:
#         print('Move Error')
#
# MP(1381, 326)
