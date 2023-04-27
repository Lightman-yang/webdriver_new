import pyautogui as p


def matcha(self, bb, aa):
    yuan = ac.imread(bb)
    mubi = ac.imread(aa)
    result = ac.find_template(yuan, mubi, 0.7)  # 0.7相似度
    if (result != None):
        return result['result'][0], result['result'][1]
        # return yuan.shape[1],yuan.shape[0]
    return None


def getsd(self):
    img = p.screenshot(region=[994, 194, 1028, 252])
    # 保存到本地
    img.save(r"./mm.png")
    return None


if __name__ == '__main__':
    import cv2 as ac

    a = 'mm'
    img_path = ('D:/webdriver_new/venv/666.png')
    # img_path=ac.imread("D:/webdriver_new/venv/666.png")
    getsd('')
    img_path2 = ('D:/webdriver_new/venv/mm.png')
    matcha(img_path, img_path2)
