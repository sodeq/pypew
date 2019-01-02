#! python script

import datetime as dt
import numpy as np
import pandas_datareader as pdr

endDate = dt.datetime.now()
nDaysAgo = 10
startDate = (endDate - dt.timedelta(days = nDaysAgo))

print(endDate.date())
print(startDate.date())

df = pdr.data.DataReader('CPIN.JK', 'yahoo', startDate, endDate)

print(df.tail(5))
