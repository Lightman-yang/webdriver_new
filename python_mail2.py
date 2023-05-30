import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_user = "1074952101@qq.com"  # 用户名
mail_pass = "uewdydfgwvakghhf"  # 口令
content = """<h2 style="color:#f00">这个一封信</h2
"""
subject = '发送测试邮件'
receivers = ['286224275@qq.com']
# def sendMail(receivers, subject, content):

'''
@param:
receivers	list	邮件接收方的邮箱列表， eg. ['****@qq.com', '*****@163.com']
subject		str		发送的邮件主题
content		str		发送的邮件内容
'''
mail_host = "smtp.qq.com"  # 设置服务器

message = MIMEText(content, 'html', 'utf-8')
# message['From'] = "1074952101@qq.com" #正确代码
# message['To'] = "286224275@qq.com"  #正确代码
# 用Header不行，后来我直接去掉Header 直接用邮箱地址，就能正常执行了发送了

message['From'] = Header('light')  # 错误
message['To'] = Header('阳')  # 错误
message['Subject'] = subject

smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtpObj.login(mail_user, "uewdydfgwvakghhf")

smtpObj.sendmail(mail_user, receivers, message.as_string())
print("邮件发送成功")
smtpObj.quit()
# try:

# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")

# if __name__ == '__main__':
#     # 第三方 SMTP 服务
#
#
#     user_info = ['286224275qq.com']
#     sendMail(user_info,'测试','测试数据...')
