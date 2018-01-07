#! python2
#-*- coding:utf-8 –*-
import tushare as ts
import time
import datetime
import common

now=datetime.datetime.now()
delta=datetime.timedelta(days=-90)
n_days=now+delta
day90 = n_days.strftime('%Y-%m-%d')

basics = ts.get_stock_basics()
basics = basics[ basics['pe'] < 41]
basics = basics[ basics['pe'] > 0]
basics = basics[basics['pb'] < 5]
basics = basics[basics['pb'] > 0]
basics = basics[basics['rev'] > 0]
basics = basics[basics['profit'] > 0]
basics = basics[basics['industry'] <> '区域地产']
basics = basics[basics['industry'] <> '全国地产']
basics = basics[basics['industry'] <> '银行']
#print basics
codes = [];
pe41 = basics.index
#common.allcode
for code in pe41:
    df = ts.get_k_data(code, start='1990-12-01')
    #print df.tail(60)['close'].max()/df.tail(60)['close'].min()
    if(df.shape[0] > 0 and df.tail(60)['close'].max()/df.tail(60)['close'].min() < 1.3):
        if (cmp(df[df['close'] > df.iat[df.shape[0] - 1, 2]]['date'].max(), day90) < 0):
            codes.append(code)
            print code

print codes



