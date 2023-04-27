import os

from comtypes.client import CreateObject

# 只支持32系统，64位注册异常
try:
    lw = CreateObject('lw.lwsoft3')
except OSError:
    path = 'C:\Windows\SysWOW64'
    # path = os.getcwd()
    # print(path)
    os.system(r'regsvr32 -s %s\lw.dll' % path)
    lw = CreateObject('lw.lwsoft3')
print(lw.ver())
