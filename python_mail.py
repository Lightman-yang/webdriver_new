import smtplib
import time
# import pandas as pd
from email.header import Header
from email.mime.text import MIMEText

"""
QQ邮箱发邮件
"""


def send_mails_QQsmtp(from_mail, to_mail, note_content, apartment_name, subject,
                      user_name, mail_host, mail_port, mymail_user, mymail_pwd):
    print(f'正在向{to_mail}发生邮件......')
    # mail msg 设置

    msg = MIMEText(note_content, 'plain', 'utf-8')
    msg['From'] = apartment_name
    msg['To'] = user_name
    msg['Subject'] = Header(subject, 'utf-8')
    with smtplib.SMTP_SSL(mail_host, mail_port) as smtObj:
        # 登陆发件人邮箱（公寓财务处邮箱）
        smtObj.login(mymail_user, mymail_pwd)
        # 发送
        smtObj.sendmail(from_mail, to_mail, msg.as_string())
        print('邮件成功发送！')


"""
    从Excel读取未缴费的用户信息，并封装返回用户信息
    例如：[['15077925650@163.com', '小张', 509, '未缴费'], ['862980997@qq.com', '二王', 511, '未缴费']]
"""

# def get_excelInfo(excel_path):
#     lists = []
#     df = pd.read_excel(excel_path)
#     # 按列查询，筛选出需要的列
#     df = df[['姓名', '房间号', '邮件', "八月"]]
#     # 取满足'未缴费'的行记录
#     rows = df.loc[df["八月"] == '未缴费']
#     for index in rows.index.values:
#         values = [rows.loc[index]['邮件'], rows.loc[index]['姓名'], rows.loc[index]['房间号'], rows.loc[index]['八月']]
#         lists.append(values)
#     return lists


if __name__ == '__main__':
    # """读取Excel"""
    # user_infos = get_excelInfo('C:\\Users\\weixiangxiang\\Desktop\\公寓用户缴费名单202108.xlsx')
    # print(user_infos)
    # """公寓信息"""
    user_info = ['286224275@qq.com']

    apartment_dict = {
        'from_mail': '1074952101@qq.com',
        # 密码pwd
        'pwd': 'uewdydfgwvakghhf',
        'sub': '通知提醒',
        'apartment_name': '1074952101@qq.com'
    }
    """查询用户信息发送邮件"""
    # 使用邮件服务商提供的SMTP服务，需要设置服务器/端口号/用户名/口令（即授权码）等
    # QQmail_host, QQmail_port = 'smtp.qq.com', 465
    QQmail_host, QQmail_port = 'smtp.qq.com', 465
    QQmail_user = apartment_dict.get('from_mail')
    QQmail_pwd = apartment_dict.get('pwd')
    apartment_name = apartment_dict.get('apartment_name')
    sub = apartment_dict.get('sub')
    to_mail = user_info[0]  # 收件邮箱
    user_name = user_info[0]  # 亲爱的xxx用户xx
    # room_no = user_info[2]  # 房间号
    note_content = f'亲爱的{1}，你好：系统显示，游戏已经崩溃了！\
                          \n{apartment_name}\
                          \n崩溃时间为{time.strftime("%Y-%m-%d %H:%M-%S秒", time.localtime())}！'
    send_mails_QQsmtp(QQmail_user, to_mail, note_content, apartment_name, sub,
                      user_name, QQmail_host, QQmail_port, QQmail_user, QQmail_pwd)
