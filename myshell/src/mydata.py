# -*- coding: utf-8 -*-
from dataapi import Client
if __name__ == "__main__":
    try:
        client = Client()
        client.init('77ac42d684c5dedeca8aa6b62a1a8714f7aeaf6def3198d3a8307f8665c9f694')
        url1='/api/market/getMktIdxd.json?field=&beginDate=20160101&endDate=20160505&indexID=&ticker=399006&tradeDate='
        code, re = client.getData(url1)
        if code==200:
            print (re)
        else:
            print (code)
            print (re)
        url2='/api/market/getMktEqud.json?field=&beginDate=20160101&endDate=20160505&secID=&ticker=000762&tradeDate='
        code, result = client.getData(url2)
        if(code==200):
            file_object = open('thefile.csv', 'w')
            file_object.write(str(result))
            file_object.close( )
        else:
            print (code)
            print (result)
    except Exception as e:
        #traceback.print_exc()
        raise e
import pandas
import tushare as ts
ts.set_token('77ac42d684c5dedeca8aa6b62a1a8714f7aeaf6def3198d3a8307f8665c9f694')
st=ts.Market()
df = st.MktEqud(tradeDate='20160505', field='ticker,secShortName,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,turnoverVol,turnoverRate')
df1=st.MktEqud(ticker='600836',beginDate='20160101',endDate='20160507',field='ticker,secShortName,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,turnoverVol,turnoverVole,turnoverRate,negMarketValue,PE,PE1,PB')
df2= ts.get_index()
print (df1)
df1.to_csv('c:/000876.csv',encoding='gbk')
