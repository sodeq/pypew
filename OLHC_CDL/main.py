import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
# from pandas.tests.io.parser import parse_dates

style.use('ggplot')

start = dt.datetime(2017, 1, 1)
end = dt.datetime(2017, 8, 31)

df = web.DataReader('JSMR.JK', 'yahoo', start, end);
# print("Reading data!")
# print(df.head())
print(df.tail(5)) # the last 5 data
# print('DONE!')
df.to_csv('JSMR.csv')
dfcsv = pd.read_csv('JSMR.csv', parse_dates = True, index_col = 0)
# we need to calculate ema
dfcsv['100ma'] = dfcsv['Close'].rolling(window=100).mean()
print(dfcsv.tail())

# create 2 plotgrids
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.plot(dfcsv.index, dfcsv['Close'])
ax1.plot(dfcsv.index, dfcsv['100ma'])
ax2.bar(dfcsv.index, dfcsv['Volume'])

# dfcsv['Close'].plot();
plt.show();


print('EXIT!!!')