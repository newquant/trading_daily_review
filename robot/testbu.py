# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk

from .utils import PoolType, MarketIndicator, Index, url_parser_data


def fetch_index_json():
    """
    指数相关信息
    :return:
    """
    index_json = url_parser_data(Index.link())
    return index_json["snapshot"]


def get_limit_up_list():
    """
    涨停相关股票
    :return:
    """
    limit_up_list = url_parser_data(PoolType.link(PoolType.limit_up))
    return limit_up_list


def get_limit_up_broken_list():
    """
    破板相关股票
    :return:
    """
    limit_up_broken_list = url_parser_data(PoolType.link(PoolType.limit_up_broken))
    return limit_up_broken_list


def fetch_market_temperature():
    """
    市场温度
    :return:
    """
    mt_list = url_parser_data(MarketIndicator.link(MarketIndicator.market_temperature))
    return round(mt_list[-1][MarketIndicator.market_temperature.name], 4)


def fetch_rise_fall_count():
    """
    上涨 ： 下跌
    :return:
    """
    rise_fall_count = url_parser_data(
        MarketIndicator.link(MarketIndicator.rise_count, MarketIndicator.fall_count))
    return "{}:{}".format(rise_fall_count[-1][MarketIndicator.rise_count.name],
                          rise_fall_count[-1][MarketIndicator.fall_count.name]) if len(rise_fall_count) >= 1 else "0:0"


def fetch_limit_up_limit_down_count():
    """
    涨停家数 ：跌停家数
    :return:
    """
    limit_up_limit_down_count = url_parser_data(
        MarketIndicator.link(MarketIndicator.limit_up_count, MarketIndicator.limit_down_count))

    return '{}:{}'.format(limit_up_limit_down_count[-1][MarketIndicator.limit_up_count.name],
                          limit_up_limit_down_count[-1][MarketIndicator.limit_down_count.name])


def fetch_limit_up_count_limit_up_broken_ration():
    """
    涨停家数，炸板率
    :return:
    """
    limit_up_count_limit_up_broken_ration = url_parser_data(
        MarketIndicator.link(MarketIndicator.limit_up_broken_count, MarketIndicator.limit_up_broken_ratio))
    return '{},{}%'.format(limit_up_count_limit_up_broken_ration[-1][MarketIndicator.limit_up_broken_count.name],
                           round(limit_up_count_limit_up_broken_ration[-1][MarketIndicator.limit_up_broken_ratio.name],
                                 2))
