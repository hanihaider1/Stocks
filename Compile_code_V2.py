# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:24:12 2021

@author: foxhe
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:06:20 2021

@author: foxhe
"""

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

    def summary(self):
      max_value = self.csv_file.loc[self.csv_file['Close'].idxmax()]
      min_value = self.csv_file.loc[self.csv_file['Close'].idxmin()]
      self.csv_file["Largest percent"]= ((self.csv_file["Close"]-self.csv_file["Open"])/self.csv_file["Close"])*100
      max_percentage = self.csv_file.loc[self.csv_file['Largest percent'].idxmax()]
      min_percentage = self.csv_file.loc[self.csv_file['Largest percent'].idxmin()]
      
      summary = {'summary': ["Price","Date"],'Highest High': [max_value["Close"],max_value["Date"]],
      'Lowest Low': [min_value["Close"],min_value["Date"]],
          'Largest Move Up%': [max_percentage["Largest percent"],max_percentage["Date"]],
          'Largest Move Downward%': [min_percentage["Largest percent"],min_percentage["Date"]],
      }
      
      df = pd.DataFrame(summary, columns = ['summary', 'Highest High','Lowest Low','Largest Move Up%','Largest Move Downward%'])
      
      return df

    # Transform the input file
    def transform(self):
        # Eliminating columns and renaming
        self.result = self.csv_file.drop(columns=["Open", "High", "Volume", "Low", "Close", "Largest percent"])
        self.result.columns = ['Date', "Price"]

        # Moving Average
        self.result['50-day MA '+self.input_file_name] = self.result.Price.rolling(window=50).mean()
        self.result['200-day MA '+self.input_file_name] = self.result.Price.rolling(window=200).mean()

        # Setting/formatting x, y axis and title
        self.result.Date = pd.to_datetime(self.result.Date)
        self.result.columns = ['Date', self.input_file_name, '50-day MA '+self.input_file_name, '200-day MA '+self.input_file_name]

    # draw plot
    def show_plot(self, another_stock):
        self.result = pd.merge(self.result, another_stock.result, on = "Date", how="inner")

        self.input_file_name += "-"+another_stock.input_file_name

        self.result.plot(x="Date")
        plt.ylabel('Price (USD)')
        plt.title(self.input_file_name + " Stock Price: 2016 - 2021")
        plt.show()


# main method
if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    # prepare StockResult object
    stock_result_sq = StockResults('SQ')
    # read input file
    stock_result_sq.read_file()
    # get summary 
    df_sq = stock_result_sq.summary()
    print("SQ Stock Performance")
    print(df_sq)

    # transform the input file
    stock_result_sq.transform()
    # show plot



    # prepare StockResult object
    stock_result_pypl = StockResults('PYPL')
    # read input file
    stock_result_pypl.read_file()
    # get summary 
    df_pq = stock_result_pypl.summary()
    print("PYPL Stock Performance")
    print(df_pq)
    # transform the input file
    stock_result_pypl.transform()


    # show plot
    stock_result_sq.show_plot(stock_result_pypl)



