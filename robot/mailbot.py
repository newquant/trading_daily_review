# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
import os
import pickle
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

home_path = os.path.expanduser("~")
file_token = os.path.join(home_path, "email.token")


def set_token(from_addr, from_addr_pwd):
    """保存调用凭证"""
    with open(file_token, 'wb') as f:
        pickle.dump([from_addr, from_addr_pwd], f)


def get_token():
    """获取调用凭证"""
    if not os.path.exists(file_token):
        raise ValueError(f"{file_token} 文件不存在，请先调用 set_token 进行设置")

    with open(file_token, 'rb') as f:
        [from_addr, from_addr_pwd] = pickle.load(f)

    return from_addr, from_addr_pwd


def attach_payload(xlsx_file: str):
    xlsx_apart = MIMEApplication(open(xlsx_file, 'rb').read())
    xlsx_apart.add_header('Content-Disposition', 'attachment', filename=xlsx_file.split("/")[-1])
    return xlsx_apart


def do_send(to_addrs: [], xlsx_file: str):
    multipart = MIMEMultipart()

    content = 'hello, this is email content.\n' \
              '每日复盘报告'
    text_apart = MIMEText(content)

    multipart.attach(text_apart)
    multipart.attach(attach_payload(xlsx_file))

    multipart['Subject'] = xlsx_file.split("/")[-1]

    try:
        server = smtplib.SMTP('smtp.qq.com')
        from_addr, from_addr_pwd = get_token()

        server.login(from_addr, from_addr_pwd)

        server.sendmail(from_addr, to_addrs, multipart.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        # 打印错误
        print('error:', e)
