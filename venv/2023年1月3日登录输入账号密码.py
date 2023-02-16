# coding=utf-8

inp_username = input('请输入用户名>>: ').strip()
inp_password = input('请输入用户密码>>: ').strip()

with open(r'D:\webdriver_new\venv\1.txt', mode='rt', encoding='utf-8') as f1:
    for lin in f1:
        username, password = lin.strip().split(':')
        if username == inp_username and password == inp_password:
            print('登录成功！')
            break
    else:
        print('账号密码不匹配！')
