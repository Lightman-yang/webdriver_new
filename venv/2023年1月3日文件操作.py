# coding='utf-8'
# with 上下文作用，mode=‘rt’ 读和操作,可以打开多个文件
# mode='at',是光标直接写数据，wt 是直接清空文件 从开头写文件
with open(r'D:\webdriver_new\venv\1.txt', encoding='utf-8', mode='rt') as f1, \
        open(r'D:\webdriver_new\venv\2.txt', encoding='utf-8', mode='rt') as f2:
    red1 = f1.read()
    red2 = f2.read()
    print(red1)
    print(red2)
