#!/usr/bin/env python  
# -*- coding:utf-8 _*- 
# Author:yanzhengbin


from email.mime.text import MIMEText
import smtplib

from_addr = "79994250@qq.com"
from_addr_pwd = "XXXXXX"   # XXXXXX为密码
smtp_server = "smtp.qq.com"
smtp_port = 465
type_dict = {"html": "html", "text": "plain"}


def send_email_to(to_addr, subject, messages, e_type):
    email_type = type_dict.get(e_type, "plain")
    msg = MIMEText(messages, email_type, 'utf-8')
    msg['Subject'] = subject
    s = smtplib.SMTP_SSL(smtp_server, port=smtp_port)
    s.login(from_addr, from_addr_pwd)
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.quit()

if __name__ == "__main__":
    send_email_to(['918886540@qq.com', 'yanzhengbin21@126.com'], 'QQ邮箱send', "<h1>如果再看你一眼，是否还会有感觉...</h1>", "html")









