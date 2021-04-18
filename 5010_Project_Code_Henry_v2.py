# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:06:20 2021

@author: foxhe
"""

#graphs and moving average

import pandas as pd
import matplotlib.pyplot as plt

ticker = input("Enter Ticker(use all caps):")
print(ticker)

#reading file
csvfile = pd.read_csv(ticker + ".csv")
df = pd.DataFrame(csvfile)

#eliminating columns and renaming 
df = df.drop(columns = ["Open","High","Volume","Low","Close"])
df.columns = ['Date','Price']

#moving average
df['50-day MA'] = df.Price.rolling(window=50).mean()
df['200-day MA'] = df.Price.rolling(window=200).mean()

#Setting/formating x, y axis and title
df.Date = pd.to_datetime(df.Date)
df.plot(x="Date")
plt.ylabel('Price (USD)')
plt.title(ticker + " Stock Price: 2016 - 2021")

plt.show()

#data table summary


df2 = pd.DataFrame(csvfile)

#df.columns = ['Date','Price']

def table_summary(df2):
    for value in df2.columns:
        max_value = df2["Close"].max()
        format_max_value = "${:.2f}".format(max_value)
        min_value = df2["Close"].min()
        format_min_value = "${:.2f}".format(min_value)
        mean_value = df2["Close"].mean()
        format_min_mean = "${:.2f}".format(mean_value)
        result = pd.DataFrame([format_max_value,format_min_value,format_min_mean], index=['Stock Price: Max ',
                              'Stock Price: Min ',
                              'Stock Price: Mean ',
                           ], columns = ["Stock Price"])
        return result
print(table_summary(df2))

df3 = pd.DataFrame(csvfile)

#df.columns = ['Date','Price']

def table_summary(df3):
    for value in df3.columns:
        vol_max = df3['Volume'].max()
        format_vol_max = "{:,.2f}".format(vol_max)
        vol_min = df3['Volume'].min()
        format_vol_min = "{:,.2f}".format(vol_min)
        vol_mean = df3["Volume"].mean()
        format_vol_mean = "{:,.2f}".format(vol_mean)
        result = pd.DataFrame([format_vol_max,format_vol_min,format_vol_mean], index=[
                              'Stock Volume: Max ',
                              'Stock Volume: Min',
                              'Stock Volume: Mean ',
                              ], columns = ["Stock volume"])
        return result
print(table_summary(df3))




    
#%%


import pandas as pd
import matplotlib.pyplot as plt


# Prepare Graphs and Moving average
class StockResults:

    def __init__(self, filename):
        self.input_file_name = filename
        self.csv_file = None
        self.result = None

    # Reading file
    def read_file(self):
        self.csv_file = pd.read_csv(self.input_file_name + ".csv")

    # Transform the input file
    def transform(self):
        # Eliminating columns and renaming
        self.result = self.csv_file.drop(columns=["Open", "High", "Volume", "Low", "Close"])
        self.result.columns = ['Date', 'Price']

        # Moving Average
        self.result['50-day MA'] = self.result.Price.rolling(window=50).mean()
        self.result['200-day MA'] = self.result.Price.rolling(window=200).mean()

        # Setting/formatting x, y axis and title
        self.result.Date = pd.to_datetime(self.result.Date)

    # draw plot
    def show_plot(self):
        self.result.plot(x="Date")
        plt.ylabel('Price (USD)')
        plt.title(self.input_file_name + " Stock Price: 2016 - 2021")
        plt.show()


# main method
if __name__ == '__main__':
    file_name = input("enter ticker filename [use all caps]:")
    print("input file name: " + file_name)
    # prepare StockResult object
    stock_result = StockResults(file_name)
    # read input file
    stock_result.read_file()
    # transform the input file
    stock_result.transform()
    # show plot
    stock_result.show_plot()
















