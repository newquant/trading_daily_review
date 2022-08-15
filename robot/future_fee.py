# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
import re
import time
import requests
import pandas as pd
import numpy as np

page = requests.get("https://www.9qihuo.com/qihuoshouxufeisingle?heyue=ag")
symbol_list = re.compile(r"""qihuoshouxufeisingle.heyue=(.*?)" target="_blank""").findall(page.text)
print(symbol_list)
dfs = pd.DataFrame()
for symbol in symbol_list:
    print(symbol)
    time.sleep(1)
    try:
        df = pd.read_html(requests.get("http://www.9qihuo.com/qihuoshouxufeisingle?heyue=" + symbol).text)[0].iloc[3:, ::]
        df = df.rename(
            columns={
                0: "合约品种", 1: "现价", 2: "涨/跌停板", 3: "买开保证金",
                4: "卖开保证金", 5: "每手保证金", 6: "开仓手续费",
                7: "平昨手续费", 8: "平今手续费", 9: "每跳毛利/元",
                10: "开平手续费", 11: "每跳净利润", 12: "是否是主力合约"
            }
        )
        dfs = dfs.append(df)
    except:
        print(f"缺失{symbol}的数据")


# 保存数据
dfs[dfs['是否是主力合约'] == "主力合约"].to_csv("../data/当前主力合约的保证金及手续费.csv", index=False)

# dfs.to_csv("../data/所有合约的保证金及手续费.csv", index=False)
