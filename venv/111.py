import pyautogui

# 查看所有支持按键
'''
200 790 <class 'tuple'>
788164
5080 10548
'''
while True:
    # print(datetime.now())
    try:
        x, y = pyautogui.locateCenterOnScreen('jinbi222.bmp', region=(200, 790, 20, 20), confidence=0.7)
        # pyautogui.keyDown('l')
        # pyautogui.keyUp('l')
        print("true")
    except:
        print("wrong")
