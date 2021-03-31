
# import the libr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# load the data
file = pd.read_csv("Google.csv")

#show data
#content = file.read()
#print(file)

# set the date as the index
file = file.set_index(pd.DatetimeIndex(file['Date'].values))
#print(file)

# create function to calculate the SMA and EMA
# and create the simple moving average (SMA)

#The MA – or ‘simple moving average’ (SMA) – is an indicator used to identify
# the direction of a current price trend, without the interference of shorter-term price spikes. The MA indicator combines price points of
# a financial instrument over a specified time frame and divides it by the number of data points to present a single trend line.


def sma(data, period=30, column='Close'):
    return data[column].rolling(window=period).mean()

# create the exponential moving average


def ema(data, period=20, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()

#  Calculating the moving convergence/ divergence (MACD)


def macd(data, period_long=26, period_short=12, period_signal=9, column='Close'):
    # calculate the short term exponential moving average
    short_ema = ema(data, period_short, column=column)
    # calculate the long term exponential moving average
    long_ema = ema(data, period_long, column=column)
    # calculate the moving average convergence / divergence(MACD)
    data['MACD'] = short_ema - long_ema
    # calculate the signal line
    data['signal_line'] = ema(data, period_signal, column='MACD')
    return data

# create the function to compute the relative strength index (RSI)


def rsi(data, period=14, column='Close'):
    delta = data[column].diff(1)
    delta = delta[1:]
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    data['up'] = up
    data['down'] = down
    avg_gain = sma(data, period, column='up')
    avg_loss = abs(sma(data, period, column='down'))
    rs = avg_gain/avg_loss
    rsi = 100.0 - (100.0/(1.0 + rs))

    data['RSI'] = rsi

    return data

# creating/adding the data set


macd(file)
rsi(file)
file['SMA'] = sma(file)
file['EMA'] = ema(file)

# show the data
# print(file)

# plot the chart MACD
column_list = ['MACD', 'signal_line']
file[column_list].plot(figsize=(12.2, 6.4))
plt.title('MACD for Google_Derrick')
plt.ylabel('USD price')
plt.xlabel('Date')
plt.show()
# plot the chart SMA
column_list = ['SMA', 'Close']
file[column_list].plot(figsize=(12.2, 6.4))
plt.title('SMA for Google_Derrick')
plt.ylabel('USD price')
plt.xlabel('Date')
plt.show()


# plot the chart EMA
column_list = ['EMA', 'Close']
file[column_list].plot(figsize=(12.2, 6.4))
plt.title('EMA for Google_Derrick')
plt.ylabel('USD price')
plt.xlabel('Date')
plt.show()

# plot the chart RSI
column_list = ['RSI']
file[column_list].plot(figsize=(12.2, 6.4))
plt.title('RSI for Google_Derrick')
plt.ylabel('USD price')
plt.xlabel('Date')
plt.show()


















