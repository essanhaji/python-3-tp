"""My final project is about pulling real time market data, minute by minute, from the stock market using Python and
alpha vantage API """

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'U5IOFGI07YAZNJWO'

# minute by minute data of Microsoft stock
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
# show data
print(data)

# get minute by minute data and save into a csv file
i = 1

# while i==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#    data.to_excel("output.xlsx")
#    time.sleep(60)

# find the volatility of stocks
close_data = data['4. close']
# get the percent change of the closing values in real time
percentage_change = close_data.pct_change()

print(percentage_change)

# what we care about actually is the last value of change
last_change = percentage_change[-1]

# we'll get an alert msg if the last change > 0.0004
if abs(last_change) > 0.0004:
    print("MSFT Alert:" + str(last_change))
