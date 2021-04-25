import pandas as pd 
import numpy as np 

class Stocks:
    '''

    Attributes: 
    stocks_ filename: this will have all the data for the stock which we want the data to be presented 
    major_index :
    This will have the file **(please add info for it i don't know have what will the data have )
    Methods :
    1)	Summary 
    2)	Rasing error
    3)	Graphs
    4)	Moving average
    5)	Comparing stocks summary
    6)	Comparing stocks graph
    '''


    def __init__(self, stocks_filename: str, major_index: str):
        '''

        Constructor: creates an new instance for stock
        parameter :
        Self -- the current object 
        stocks _filename:string -- the data for the stocks 
        major _index:string -- the data for major index
        '''
        #add code to raise error 

        self.read_stock_file = pd.read_csv(stocks_filename)
        self.read_major_index = pd.read_csv(major_index)

    def test(self):
        value = self.read_stock_file["High"]
        return max(value)

    def rasing_error(self):
        '''
        parameter:
        self -- the current object 
        his will raise any error, this method will
        be called in all the method or that we can raise error
        '''
        pass


    def summary(self):
        '''
        Method:summary: gets the complete summary of stocks 
        Parameter:
        Self-- the current object:
        Returns the complete summary which will have stock price and date, where 
        it was  highest stock, lowest stock, largest moving up in a single day
        % and largest moving downward in a single day by %
        '''
        pass
    
    def graph(self, start_date=self.start_date, end_date=self.end_date):
        '''Method -- graph
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns a line graph of the stock prices 
        '''
        pass


    def moving_average(self, start_date=self.start_date, end_date=self.end_date):
        '''
        Method -- moving average
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns the moving average of the stocks 
        '''
        pass


    def comparing_stocks(self, comparing_stock_filename):
        '''Method -- comparing_stocks 
        parameters :
        Comparing_stock_filename-- file we are going to compare with
        Returns *** need to discuss what should be returning 
        '''
        pass


    def comparing_stocks_graph(self, start_date=self.start_date, end_date=self.end_date):
        '''Method -- comparing_stocks_graphs 
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns a line graph of the stock prices 
        '''
        pass


def main():
    
    value = Stocks("SQ (1).csv","asd")
    eg = value.test()
    print(eg)
main()
