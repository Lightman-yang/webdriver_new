import time

import numpy as np
import pyautogui
from PIL import Image

b = time.strftime("%y-%m-%d_%H$%M$%S", time.localtime())

img = pyautogui.screenshot(region=[48, 84, 848, 684])
img = Image.fromarray(np.uint8(img))
img.save('D:\webdriver_new\lw\Tpshot{}s.png'.format(b))

print(b)
