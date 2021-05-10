# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
import json
import time
from enum import Enum

import requests


def url_parser(uri: str) -> json:
    return json.loads(requests.get(uri).content)


def url_parser_data(uri: str) -> json:
    return json.loads(requests.get(uri).content)['data']


def handle_date_time(timestamp: float):
    d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))[-8:]
    return d


def handle_e(num: int):
    n = str(round(num / 100000000, 2)) + '亿'
    return n


def handle_percent(float_num: float):
    s = str(round(float_num * 100, 2)) + '%'
    return s


class PoolType(Enum):
    limit_up = '涨停池'
    limit_up_broken = '炸板池'
    yesterday_limit_up = '昨日涨停'
    super_stock = '强势股票池'
    limit_down = '跌停池'
    new_stock = '新股池'
    nearly_new = '次新股池'

    @staticmethod
    def link(*kwargs):
        pool = ",".join([i.name for i in kwargs])
        return 'https://flash-api.xuangubao.cn/api/pool/detail?pool_name=' + pool


class MarketIndicator(Enum):
    rise_count = '上涨家数'
    fall_count = '下跌家数'
    limit_up_count = '涨停家数'
    limit_down_count = '跌停家数'
    limit_up_broken_count = '破板家数'
    limit_up_broken_ratio = '破板率'
    market_temperature = '市场温度'

    @staticmethod
    def link(*kwargs):
        indicator = ",".join([i.name for i in kwargs])
        return 'https://flash-api.xuangubao.cn/api/market_indicator/line?fields=' + indicator


class Index(Enum):
    prod_code = ['000001.SS,399001.SZ,399006.SZ']
    fields = ['prod_name,last_px,px_change,px_change_rate']

    @staticmethod
    def link():
        return 'https://api-ddc-wscn.xuangubao.cn/market/real?' + Index.prod_code.name + '=' + ','.join(
            Index.prod_code.value) + "&" + Index.fields.name + '=' + ','.join(Index.fields.value)
