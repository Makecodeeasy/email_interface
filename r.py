#!/usr/bin/env python  
# -*- coding:utf-8 _*- 
# Author:yanzhengbin

import requests

url = "http://127.0.0.1:5000/send_mail"
data = {
        "to_addr": "918886540@qq.com",
        "subject": "放学别走",
        "messages": "<h1>有种放学别走</h1>",
        "e_type": "html",
}


r = requests.post(url=url, data=data)
print r.text