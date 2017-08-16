#!/usr/bin/env python
# coding:utf-8

from flask import Flask
from flask import request
from email_sender import send_email_to

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_mail', methods=['GET', 'POST'])
def send_email():
    if request.method == "POST":
        print request.method
        to_addr = request.form.get('to_addr', None)
        subject = request.form.get('subject', None)
        messages = request.form.get('messages', None)
        e_type = request.form.get('e_type', None)
        if not all([to_addr, subject, messages, e_type]):
            return "请求参数有误。。。"
        else:
            try:
                send_email_to(to_addr, subject, messages, e_type)
                return "发送邮件成功"
            except Exception, e:
                return "发送邮件失败,%s" % e
    else:
        return "不允许的请求..."

if __name__ == '__main__':
    app.run()
