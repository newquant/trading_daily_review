# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
from pprint import pprint

import requests

from robot.kpl import api_path_prefix


def data1():
    data = {
        'c': 'IndexPlate',
        'a': 'GetIndexList',
        'view': '1%2C2%2C3',
        'st': '2',
        'Type': '0',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3',
    }

    resp = requests.post(url=api_path_prefix.article_url,
                         data=data).json()
    pprint(resp)


def data2():
    data = {
        'c': 'ThemeNews',
        'a': 'GetThemeStaus',
        'NID': '2-2%2C2-4',
        'DeviceID': 'ffffffff-ffe2-caf2-0000-0000449f1be3',
    }

    resp = requests.post(url=api_path_prefix.article_url,
                         data=data).json()
    pprint(resp)


if __name__ == '__main__':
    data2()
