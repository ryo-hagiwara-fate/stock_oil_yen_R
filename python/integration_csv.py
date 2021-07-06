import pandas as pd
import numpy as np

oil = pd.read_csv('../datasets/原油先物 WTI 過去データ.csv')
average_stock_price = pd.read_csv('../datasets/日経平均株価 過去データ.csv')
usd_jpy = pd.read_csv("../datasets/USD_JPY 過去データ.csv")

# 日付でcsvを結合
# FIXME: 一括マージ
mergedData = pd.merge(oil, average_stock_price,on='日付け')
mergedData2 = pd.merge(mergedData, usd_jpy,on='日付け')


# 日付、原油終値、日経平均株価終値以外の列を削除
analysis_data = mergedData2.drop(columns=mergedData2.columns[[2,3,4,5,6,8,9,10,11,12,14,15,16,17]])

for i in range(len(analysis_data["stock_終値"])):
    analysis_data["stock_終値"][i] = analysis_data["stock_終値"][i].replace(',','')

analysis_data.to_csv("../datasets/oil_stock_yen.csv")