#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/4/7 15:45
import os
import win32api
import time
import win32gui
#65900|Shell_TrayWnd
import win32com
import win32clipboard as w
import win32con
import time

# u=pyautogui.size()
# print(u)
# pyautogui.hotkey('alt','l')
# pyautogui.press('l')
# #pyautogui.press('alt')+pyautogui.press("l")
# pyautogui.alert('这个消息弹窗是文字+OK按钮')

key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    'F1': 112, 'F2': 113, 'F3': 114, 'F4': 115, 'F5': 116, 'F6': 117, 'F7': 118, 'F8': 119,
    'F9': 120, 'F10': 121, 'F11': 122, 'F12': 123, 'F13': 124, 'F14': 125, 'F15': 126, 'F16': 127,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
    'BACKSPACE': 8, 'TAB': 9, 'TABLE': 9, 'CLEAR': 12,
    'ENTER': 13, 'SHIFT': 16, 'CTRL': 17,
    'CONTROL': 17, 'ALT': 18, 'ALTER': 18, 'PAUSE': 19, 'BREAK': 19, 'CAPSLK': 20, 'CAPSLOCK': 20, 'ESC': 27,
    'SPACE': 32, 'SPACEBAR': 32, 'PGUP': 33, 'PAGEUP': 33, 'PGDN': 34, 'PAGEDOWN': 34, 'END': 35, 'HOME': 36,
    'LEFT': 37, 'UP': 38, 'RIGHT': 39, 'DOWN': 40, 'SELECT': 41, 'PRTSC': 42, 'PRINTSCREEN': 42, 'SYSRQ': 42,
    'SYSTEMREQUEST': 42, 'EXECUTE': 43, 'SNAPSHOT': 44, 'INSERT': 45, 'DELETE': 46, 'HELP': 47, 'WIN': 91,
    'WINDOWS': 91, 'NMLK': 144,
    'NUMLK': 144, 'NUMLOCK': 144, 'SCRLK': 145,
    '[': 219, ']': 221, '+': 107, '-': 109}

combine_keys = {
    ('CONTROL', 'G'): "创建组合", ('CONTROL', 'ALT', 'G'): "创建为画板", ('CONTROL', 'ALT', 'K'): "创建组件",
    ('CONTROL', 'E'): "路径拼合",
    ('CONTROL', 'SHIFT', 'G'): "取消组合", ('CONTROL', 'ALT', 'M'): "创建蒙版", ('CONTROL', 'SHIFT', 'O'): "轮廓描边",
    ('CONTROL', ']'): "上移一层", ('CONTROL', '['): "下移一层", ('CONTROL', 'SHIFT', ']'): "移至顶层",
    ('CONTROL', 'SHIFT', '['): "移至底层",
    ('CONTROL', 'SHIFT', 'H'): "显示/隐藏图层", ('CONTROL', 'SHIFT', 'L'): "锁定/解锁", ('SHIFT', 'H'): "水平翻转",
    ('SHIFT', 'V'): "垂直翻转",
    ('DELETE'): "删除", ('SHIFT', 'L'): "箭头", ('CONTROL', 'ALT', 'SHIFT', 'V'): "垂直等距分布",
    ('CONTROL', 'ALT', 'SHIFT', 'H'): "水平等距分布"
}


def release_key(key_code):
    """
        函数功能：抬起按键
        参   数：key:按键值
    """
    win32api.keybd_event(key_code, win32api.MapVirtualKey(key_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def press_key(key_code):
    """
        函数功能：按下按键
        参   数：key:按键值
    """
    win32api.keybd_event(key_code, win32api.MapVirtualKey(key_code, 0), 0, 0)


def press_and_release_key(key_code):
    """
        按一下按键
    :param key_code: 按键值，如91,代表WIN windows系统的系统按键，弹出开始菜单
    :return:
    """
    press_key(key_code)
    release_key(key_code)


def pressKey(key):
    """
    点击按键（按下并抬起）
    :param key: 按键,如:F5,ENTER
    :return:
    """
    if isinstance(key, str):
        press_and_release_key(key_map[key.upper()])
    elif isinstance(key, int):
        press_and_release_key(key)


def press_keys(*args):
    """
    按下组合键 支持多个字符，数组，元组类型
    :param args: 例如： ALT，TAB
    :return:
    """
    for i in args:
        if isinstance(i, str):
            press_key(key_map.get(i))
            time.sleep(0.3)
        elif isinstance(i, list):
            [press_keys(n) for n in i]
        elif isinstance(i, tuple):
            [press_keys(n) for n in i]


def release_keys(*args):
    """
    松开组合键 支持多个字符，数组，元组类型
    :param args: 例如：ALT，TAB
    :return:
    """
    for i in args:
        if isinstance(i, str):
            release_key(key_map.get(i))
        elif isinstance(i, list):
            [release_keys(n) for n in i]
        elif isinstance(i, tuple):
            [press_keys(n) for n in i]
if __name__ == '__main__':
    print(time.strftime("%Y/%m/%d %H:%M:%S"))
    print(time.localtime())
    A = os.system(r'"C:\Program Files (x86)\Huawei\HDPClient\CloudClient.exe"')

    #B=os.system(r'"D:\软件文件包\Dict\YoudaoDict.exe"')

    # time.sleep(4)

    # FrameClass = "QWidget"
    # FrameTitle = "地址管理"
    #hwnd = win32gui.FindWindow(1837274, FrameTitle)
    # hwnd = win32gui.FindWindow(70208,"网易有道词典")
    # 65900  197706,"Shell_TrayWnd "QWidget","地址管理"
    # handle.win32gui.SetForegroundWindow()
    # win32gui.SetForegroundWindow(hwnd)
    # print(hwnd)
    # k.press_key(k.alt_key)# 按住alt键
    # k.press_key('l')# 模拟键盘按l键
    # k.release_key(k.alt_key)   # 松开alt键
    time.sleep(4)
    release_keys('ALT',"L")
    pressKey('L')


    # win32gui.ShowWindow(handle,win32con.SW_MAXIMIZE)
    #hwnd.press_keys(18,76)
    # press_and_release_key(13)
    # pressKey(76)
    # release_key(18)