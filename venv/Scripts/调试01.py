import time
import pyautogui
import pydirectinput as Qt
import time

import pyautogui
import pydirectinput as Qt

Qt.FAILSAFE = True
pyautogui.FAILSAFE = True


# def find_screen(ppp,random_aa):
def find_screen(ppp):
    try:
        time.sleep(0.5)  # 等待 0.5 秒
        # zuuu = pyautogui.locateOnScreen(ppp,confidence=random_aa)  # 寻找 点赞图片；
        zuuu = pyautogui.locateOnScreen(ppp, confidence=0.8, )  # 寻找 点赞图片；
        ceQter = pyautogui.center(zuuu)  # 寻找 图片的中心
        print('找到了', ceQter, )
        return ceQter
    except:
        ceQter = 0
        print('没找到')
        return ceQter


def click_screen(ppp):
    x_y = find_screen(ppp)
    if x_y == 0:
        print('没有图片')

    else:
        pyautogui.click(x_y, duration=3)  # duration是用多少秒点划过去


if __name__ == '__main__':
    for i in range(1, 20):
        find_screen('鞋子.png')
        find_screen('鞋子2.png')
        find_screen('鞋子3.png')
        find_screen('鞋子4.png')
        find_screen('鞋子5.png')
    '''
    #金币坐标 x y(574, 473)
    # 获取当前鼠标【x y】坐标 309 118
    time.sleep(5)
    point = win32api.GetCursorPos()
    print(point)
    #通过坐标获取坐标下的【窗口句柄】
    hwnd = win32gui.WindowFromPoint(point)  # 请填写 x 和 y 坐标
    print(hwnd)

    #步骤8 通过窗口句柄 获取当前窗口的【左、上、右、下】四个方向的坐标位置
    # 通过句柄值获取当前窗口的【左、上、右、下】四个方向的坐标位置
    # left, top, right, bottom = win32gui.GetWindowRect('句柄值')
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)

    #移动鼠标
    # pyautogui.moveTo(574, 473, duration=2)

    x, y = point
    print(x, y, type(point))
    zz='screen88.png'
    for i in range(1,10):
        n=0
        xx_yy=0
        while xx_yy ==0 :
            # cc=random.uniform(0.70,1)
            cc=1
            xx_yy = find_screen(zz,cc)
            n=n+1
            print('继续{},{}'.format(n,cc))
        else:

            x1, y1 =xx_yy
            print(x1, y1, type(x1), type(y1))
            pyautogui.moveTo(x1, y1, duration=2)
            print('循环多次{}'.format(i))
            break
    print('1')

'''
