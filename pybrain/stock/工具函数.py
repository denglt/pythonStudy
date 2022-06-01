import datetime
import pandas as pd

# 计算股票量比


def quantityRelativeRatio(stockCode, dateStr):
    endDate = datetime.datetime.strptime(dateStr, "%Y-%m-%d")
    days = datetime.timedelta(days=10)
    beginDate = endDate - days
    endDate = endDate.strftime("%Y-%m-%d")
    beginDate = beginDate.strftime("%Y-%m-%d")
    df = DataAPI.MktEqudGet(secID=u"", ticker=stockCode, tradeDate=u"",
                            beginDate=beginDate, endDate=endDate, isOpen="1", field=u"", pandas="1")
    turnoverVols = df.sort_index(ascending=False).turnoverVol
    todayVol = turnoverVols.iloc[0]
    hisVol = turnoverVols.iloc[1:6].mean()
    return todayVol/hisVol


def customizedMetrics(stockDf):
    stockDf["quantityRelativeRatio"] = stockDf.apply(
        lambda row: quantityRelativeRatio(row.ticker, row.tradeDate), axis=1)
    return stockDf


def nextDate(dateStr):
    nextDate = datetime.datetime.strptime(
        dateStr, "%Y-%m-%d") + datetime.timedelta(days=1)
    return nextDate.strftime("%Y-%m-%d")


def hisStockInfo(stockCodes, dateStr):
    endDate = datetime.datetime.strptime(
        dateStr, "%Y-%m-%d") - datetime.timedelta(days=1)
    beginDate = endDate - datetime.timedelta(days=10)
    endDate = endDate.strftime("%Y-%m-%d")
    beginDate = beginDate.strftime("%Y-%m-%d")
    stockDf = DataAPI.MktEqudGet(secID=u"", ticker=stockCodes, tradeDate=u"",
                                 beginDate=beginDate, endDate=endDate, isOpen="", field=u"", pandas="1")
    stockDf.sort_values(by=['ticker', 'tradeDate'],
                        ascending=False, inplace=True)
    stocks = dict()
    for index, r in stockDf.iterrows():
        stock = stocks.get(r.ticker)
        if (stock == None):
            stock = dict()
            stock["num"] = 1
            stocks[r.ticker] = stock
        else:
            stock["num"] = stock["num"] + 1

        stock["pre_" + str(stock["num"]) + "_turnoverVol"] = r.turnoverVol
        # stock["pre_" + str(stock["num"]) +"_tradeDate"] = r.tradeDate

    return pd.DataFrame.from_dict(stocks, orient='index')


def quantityRelativeRatio_old(stockCode, dateStr):
    endDate = datetime.datetime.strptime(dateStr, "%Y-%m-%d")
    days = datetime.timedelta(days=10)
    beginDate = endDate - days
    endDate = endDate.strftime("%Y-%m-%d")
    beginDate = beginDate.strftime("%Y-%m-%d")
    # print(beginDate,endDate)
    df = DataAPI.MktEqudGet(secID=u"", ticker=stockCode, tradeDate=u"",
                            beginDate=beginDate, endDate=endDate, isOpen="1", field=u"", pandas="1")
    turnoverVols = df.sort_index(ascending=False).turnoverVol
    todayVol = turnoverVols.iloc[0]
    hisVols = turnoverVols.iloc[1:6]
    hisVol = hisVols.sum()/float(hisVols.size)  # python 2.x 除法"/" 会自动取整数
    # print(todayVol,hisVol)
    return todayVol/hisVol
