#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/5/20 17:10
import os
import time

from fuzzywuzzy import fuzz
# q=1
#
# while q<2:
#     z = input("abc:")
#     x="新标签页 n"


import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.238.232.133', port=22, username='iaas', password='iaas@123')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果


res, err = stdout.read(), stderr.read()
result = res if res else err

print(str(res,encoding='utf-8'))
time.sleep(2)
#执行‘ls’命令
stdin, stdout, stderr=ssh.exec_command("ls")
res1=stdout.read()
print(res1.decode())
#执行"ps -ef|grep tomccat"命令
time.sleep(2)
stdout,stderr=ssh.exec_command("ps -ef|grep tomcat")
res2,err2= stdout1.read(),stderr2.read()
result2 = res2 if res2 else err2
res2=stdout.read()
print(str(result2,encoding='utf-8'))


