import tushare as ts
import urllib
import urllib2
import json

class Stock(object):
    """docstring for Hotel"""
    def __init__(self, code,open,current,high,low,date,clmn=0):
        self.code = code
        self.open = open
        self.current = current
        self.high = high
        self.low = low
        self.clmn = clmn
        self.date = date

basics = ts.get_stock_basics()

for code in basics.index:
    df = ts.get_k_data(code, start='1990-12-01')
    #print df
    stocks = []
    for item in df.values:
        stocks.append(Stock(item[6],item[1],item[2],item[3],item[4],item[0],item[5]))

    stocks_data = {'stocks': json.dumps(stocks,default=lambda obj: obj.__dict__)}
    test_data_urlencode = urllib.urlencode(stocks_data)

    requrl = "http://ichess.sinaapp.com/daily/recordDaily.php"

    req = urllib2.Request(url=requrl, data=test_data_urlencode)

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print code





