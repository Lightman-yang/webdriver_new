#_*_ coding: UTF-8 _*_
#开发人员  :light
#开发时间  :2021/8/24 15:03


import paramiko
client=paramiko.SSHClient()   #创建一个客户端client对象
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname='10.238.232.133',port=22,username='iaas',password='iaas@123')
print()
# stdout 为正确输出，stderr为错误输出，同时是有1个变量有值 'ls'查看

stdin,stdout,stderr = client.exec_command('ls')
print(stdout.read().decode('utf-8'))

"""
#进入高级权限：sudo -s
stdin,stdout,stderr = client.exec_command('sudo -s')
print(stdout.read().decode('utf-8'))

#1，进入停止app服务： cd tomcat-app/webapps/
stdin,stdout,stderr = client.exec_command('./tomcat-app/bin/shutdown.sh')
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))
print(stdin.read().decode('utf-8'))


#2.启动app服务
stdin,stdout,stderr = client.exec_command('sudo ./tomcat-app/bin/startup.sh')
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))
print(stdin.read().decode('utf-8'))
"""
"""
#3.删除app服务文件
stdin,stdout,stderr = client.exec_command('sudo rm -rf /home/iaas/tomcat-app/webapps/ROOT/')
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))
print(stdin.read().decode('utf-8'))
#remove('/home/iaas/tomcat-app/webapps/ROOT/')
"""



#sudo -s
#ls
#cd tomcat-app/webapps/
#../bin/shutdown.sh
#rm lcpmapp lcpmapp.war ROOT
#y
#../bin/startup.sh
#ps -ef|grep tomcat

client.close()