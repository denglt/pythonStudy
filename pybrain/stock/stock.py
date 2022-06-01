import easyquotation

import pandas as pd


def reload():
    quotation = easyquotation.use('qq')
    ## quotation = easyquotation.use('sina')

    ## stocks = quotation.stocks(['601939', '601398'])

    stocks = quotation.market_snapshot(prefix=False)

    """
    for stock_code in stocks.keys():
        print(stock_code)
        for k in stocks[stock_code]:
            v = stocks[stock_code][k]
            print(k, ":", v, type(v))
    """

    """
    # dict 转换 为 list of dict
    stockList = list()
    indexes = list()
    for stock_code in stocks.keys():
        stockList.append(stocks[stock_code])
        indexes.append(stock_code)

    # From a list of dicts
    stockDf = pd.DataFrame(stockList, index=indexes)
    """
    global allStock
    allStock = pd.DataFrame.from_dict(stocks, orient='index')  # 该一句实现上面 注释代码

    # ssDf.loc["sz000001"]   // select row

    # negMarketValue	float	流通市值，收盘价*无限售流通股数
    # marketValue	float	总市值，收盘价*总股本数
    # turnoverRate	float	换手率，成交量/无限售流通股数
    # chgPct	float	涨跌幅，收盘价/昨收盘价-1
    # PE	动市盈率，即市盈率TTM，总市值/归属于母公司所有者的净利润TTM
    # PE1	动态市盈率，总市值/归属于母公司所有者的净利润（最新一期财报年化）
    # PE2   静态市盈率
    # PB	市净率，总市值/归属于母公司所有者权益合计
    # turnoverVol	成交量
    # turnoverValue	成交金额，A股单位为元，B股单位为美元或港币
    # openPrice	float	开盘价
    # highestPrice	float	最高价
    # lowestPrice	float	最低价
    # closePrice	float	收盘价

    allStock["chgPct"] = allStock["涨跌(%)"]/100
    allStock["turnoverRate"] = allStock.turnover/100
    allStock["marketValue"] = allStock.总市值 * 100000000
    allStock["negMarketValue"] = allStock.流通市值 * 100000000

    allStock = allStock.rename(
        columns={
            '成交量(手)': 'turnoverVol',
            '成交额(万)': 'turnoverValue',
            '市盈(动)': 'PE1',
            '市盈(静)': 'PE2',
            'open': 'openPrice',
            'close': 'closePrice',
            'high': 'highestPrice',
            'low': 'lowestPrice',
            '量比': 'quantityRatio',
        })

    # selectStock = stockDf.loc[stockDf.chgPct > 0.03]

    global condition
    condition = 'chgPct > 0.03 and chgPct < 0.05 and quantityRatio >= 1 and turnoverRate > 0.05 and turnoverRate < 0.1 and negMarketValue > 5000000000  and negMarketValue < 20000000000'

    global selectStock
    selectStock = allStock.query(condition)

    """
    useStock = selectStock.drop(['code', 'volume', 'bid_volume', 'ask_volume', 'bid1', 'bid1_volume', 'bid2',
                                'bid2_volume', 'bid3', 'bid3_volume', 'bid4', 'bid4_volume', 'bid5',
                                'bid5_volume', 'ask1', 'ask1_volume', 'ask2', 'ask2_volume', 'ask3',
                                'ask3_volume', 'ask4', 'ask4_volume', 'ask5', 'ask5_volume', '最近逐笔成交',
                                '涨跌', '涨跌(%)', 'turnover',
                                '价格/成交量(手)/成交额', 'unknown', 'high_2', 'low_2', '振幅', '流通市值', '总市值', '涨停价', '跌停价',
                                '委差', '均价'], axis=1)
    """

    fields = ["name", "now", "openPrice", "lowestPrice", "highestPrice", "chgPct", "turnoverRate", "PE",
              "PE1", "PE2", "PB", "quantityRatio", "turnoverVol", "turnoverValue", "marketValue", "negMarketValue"]
    global selectS
    global alls
    selectS = selectStock[fields]
    allS = allStock[fields]


helpStr = '''
  allStock: 全部股票 ; allS: 全部股票 （仅关键字段）
  selectStock: 选中的股票 ; selectS: 选中的股票  （仅关键字段）
  某个股票信息：allS.loc['002733']
'''

reload()

print("选股条件：" + condition)
print(helpStr)
