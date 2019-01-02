#! python script

import datetime as dt
import numpy as np
import pandas_datareader as pdr
import pandas as pd

# prompt wether to use local data or remote data (currently set to obtain  from yahoo 
# -- yahoo no longer support their finance API)
local_data = input("Using local data?(y/n) ")
if local_data == 'n':
    endDate = dt.datetime.now()
    nDaysAgo = 10
    startDate = (endDate - dt.timedelta(days = nDaysAgo))

    print(endDate.date())
    print(startDate.date())

    stockList = ['CPIN.JK', 'KAEF.JK']

    """
    Iterate over stocklist data!
    """
    for x in stockList:
        print(x)

    cpin_jk = pdr.data.DataReader(stockList[0], 'yahoo', startDate, endDate)
    kaef_jk = pdr.data.DataReader(stockList[1], 'yahoo', startDate, endDate)

    print(cpin_jk.tail(5))
    # print(kaef_jk.tail(5))

    # now filter out zero volume trading day
    
    print("Filtered for V > 0")
    print(cpin_jk[cpin_jk['Volume'] > 0].tail(5))
    
elif local_data == 'y':
    print("Using local data: JSMR.JK")
    # jsmr_jk = pd.read_csv('JSMR.csv', parse_dates = True, index_col = 0)
    dfcsv = pd.read_csv('JSMR.csv', parse_dates = True, index_col = 0)
    print(dfcsv.tail(5))
else:
    pass

