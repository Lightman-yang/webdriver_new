import pydirectinput  as Qt
import pyautogui as QQgui
# 找到了 Point(x=224, y=295)  1381, 326
import time
# 找到了 Point(x=224, y=295)  1381, 326
import time

import pyautogui as QQgui
import pydirectinput  as Qt


def left_click():
    Qt.press('Numpad_0')
    time.sleep(2)
    QQgui.press('0')
    # time.sleep(0.15)
    # QQgui.press('+')
    # time.sleep(0.15)
    # QQgui.press('num0')


if __name__ == '__main__':
    time.sleep(5)
    left_click()
    print('pass')
