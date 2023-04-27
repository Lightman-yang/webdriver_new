import time

import psutil
import win32api
import win32con
import win32gui
import win32process

'''步骤1 获取当前【鼠标坐标】'''
# 获取当前鼠标【x y】坐标 309 118
time.sleep(5)
point = win32api.GetCursorPos()

x, y = point
print(x, y, type(point))
'''步骤2 通过鼠标坐标 获取鼠标坐标下的【窗口句柄】'''

# 通过坐标获取坐标下的【窗口句柄】
hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标
print(hwnd)

'''步骤3 通过窗口句柄获取 【线程ID（hread_id）, 和 进程ID（process_id）】'''
# 通过句柄获取【线程ID 进程ID】
# hread_id, process_id = win32process.GetWindowThreadProcessId('句柄值')
hread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
print(hread_id, process_id)

'''步骤4 通过进程ID 获取【进程名称】'''
# 通过进程ID获取【进程名称】 列：weixin.exe
# process = psutil.Process('进程ID').name()
process = psutil.Process(process_id).name()
print(process)

'''步骤5 通过进程ID 获取【标准路径】'''
# 通过进程ID 获取主文件程序【标准路径】 列：D:/filed/windoee/weixin.exe
# p_bin = psutil.Process('进程ID').exe()
p_bin = psutil.Process(process_id).exe()
print(p_bin)

'''步骤6 通过进程ID 获取当前程序的【CPU利用率】'''
# 通过进程ID获取 当前程序的【CPU利用率】 列：2.928741925323
# mem_percent = psutil.Process('进程ID').memory_percent()
mem_percent = psutil.Process(process_id).memory_percent()
print(mem_percent)

'''步骤7 通过进程ID 获取当前程序的【线程数量】'''
# 通过进程ID获取 当前程序的【线程数量】
# num_threads = psutil.Process('进程ID').num_threads()
num_threads = psutil.Process(process_id).num_threads()
print(num_threads)

'''步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置'''
# 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
# left, top, right, bottom = win32gui.GetWindowRect('句柄值')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)

'''步骤9 通过标题名称【获取句柄】'''
# 通过窗口标题获取句柄
# hld = win32gui.FindWindow(None,u"此电脑")
# hld = win32gui.FindWindow(None,u"网易云音乐")
# print(hld)

'''步骤10 通过句柄 获得【标题】'''


# 通过句柄获得标题
# def get_title(hwnd):
#     title = win32gui.GetWindowText(hwnd)
#     print('窗口标题:%s' % (title))
#     return title
def get_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    print('窗口标题:%s' % (title))
    return title


'''步骤11 通过句柄获得【窗口类名】'''


# 通过句柄获取窗口类名
# def get_clasname(hwnd):
#     clasname = win32gui.GetClassName(hwnd)
#     print('窗口类名:%s' % (clasname))
#     return clasname
# get_clasname("句柄值")
# 通过句柄获取窗口类名
def get_clasname(hwnd):
    clasname = win32gui.GetClassName(hwnd)
    print('窗口类名:%s' % (clasname))
    return clasname


'''步骤12 通过句柄【置顶窗口】'''
# 通过句柄窗口置顶
# win32gui.SetWindowPos('句柄值', win32con.HWND_TOPMOST,0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)

'''步骤13 通过句柄【取消置顶窗口】'''


# 通过句柄取消窗口置顶
# def set_down(hwnd):
#     win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
#                           win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
# set_down("句柄值")
def set_down(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)


'''步骤14 通过句柄将窗口【放到最前面】（非置顶）'''
# 通过句柄将窗口放到最前
# win32gui.SetForegroundWindow("句柄值")
win32gui.SetForegroundWindow(hwnd)

'''步骤15 检测当前句柄【是否存在】返回值为 1 或 0'''
# 检测当前句柄是否存在  存在则返回  1  不存在返回 0
'''
 N = win32gui.IsWindowEnabled("句柄值")
 S = win32gui.IsWindowVisible("句柄值")
 V = win32gui.IsWindow("句柄值")
'''
N = win32gui.IsWindowEnabled(hwnd)
S = win32gui.IsWindowVisible(hwnd)
V = win32gui.IsWindow(hwnd)
print(N, S, V)

'''步骤16 通过窗口句柄【最大化和最小化窗口】'''
# 通过窗口句柄【最大化窗口】
'''
win32gui.ShowWindow('句柄值', win32con.SW_MAXIMIZE)# 通过窗口句柄【最大化窗口】
win32gui.ShowWindow('句柄值', win32con.SW_MINIMIZE) # 通过窗口句柄【最小化窗口】
'''
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
# win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

'''步骤17 通过窗口句柄【隐藏窗口和显示隐藏窗口】'''
'''
win32gui.ShowWindow('句柄值', win32con.SW_HIDE) # 通过窗口句柄【隐藏窗口】
win32gui.ShowWindow('句柄值', win32con.SW_SHOW) # 通过窗口句柄【显示隐藏窗口】
'''

'''步骤18 通过窗口句柄【关闭当前句柄控件】'''
'''
# 通过窗口句柄【关闭当前句柄控件】
# 是关闭单个句柄控件，不是关闭整个程序，只能关闭输入的句柄值
win32gui.SendMessage('句柄值', win32con.WM_CLOSE)
'''

'''步骤19 通过窗口句柄【更改窗口标题】'''
'''
# 通过句柄【更改窗口标题】 两种方法
win32gui.SetWindowText('句柄值', '名称')
win32gui.SendMessage('句柄值', 12, 0, '名称')
'''
a = '测试'
win32gui.SetWindowText(hwnd, '{}'.format(a))
print('pass')
'''步骤20 打开此文件所在文件夹并【定位到此文件】'''
'''
import subprocess
# 在打开此文件所在文件夹并【定位到此文件】
FILE = 'C:/Windows/System32/notepad.exe'
subprocess.Popen(f'explorer.exe /select,{FILE}', shell=False)
'''

'''获取某坐标的【RGB颜色值】'''
'''
import pyautogui
# 获取某坐标的RGB颜色值  返回(236, 236, 236)
pyautogui.screenshot().getpixel((x,y)) 手动填写 x y 坐标
'''
