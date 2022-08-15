# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
from pprint import pprint

import requests

from robot.kpl import api_path_prefix


def data1():
    """
    index
    :return:
    """
    data = {
        'c': 'Index',
        'a': 'NewGetList',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3'
    }

    resp = requests.post(url=api_path_prefix.lhb_url,
                         data=data).json()
    pprint(resp)
    pprint(resp['DongXiang'])


def data20():
    """
    stock
    :return:
    """
    data = {
        'c': 'Stock',
        'a': 'GetCommon',
        'Index': '0',
        'st': '30',
        'StockID': '002547',
        'Day': '2022-06-29',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3'
    }

    resp = requests.post(url=api_path_prefix.lhb_url,
                         data=data).json()
    pprint(resp)


def data21():
    data = {
        'c': 'Stock',
        'a': 'GetNewOneStockInfo',
        'Type': '0',
        'Time': '2022-08-02',
        'StockID': '002547',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3'
    }

    resp = requests.post(url=api_path_prefix.lhb_url,
                         data=data).json()
    pprint(resp)


def data22():
    """
    返回对应日期的行情数据
    :return:
    """
    'c=Stock&a=GetStockChart&StockID=002547&DeviceID=ffffffff-ffe2-caf2-0000-0000449f1be3'
    pass


def data3():
    data = {
        'c': 'UserBusiness',
        'a': 'GetDay',
        'Day': '',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3'
    }

    resp = requests.post(url=api_path_prefix.lhb_url,
                         data=data).json()
    pprint(resp)

def data31():
    """
    需要登录状态
    {'errcode': '1001', 'errmsg': '登录状态失效！'}
    :return:
    """
    data = {
        'c': 'UserBusinessGroup',
        'a': 'GetGroupList',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3'
    }

    resp = requests.post(url=api_path_prefix.lhb_url,
                         data=data).json()
    pprint(resp)

if __name__ == '__main__':
    data3()
