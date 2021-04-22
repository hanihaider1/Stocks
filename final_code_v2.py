import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

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


    def __init__(self, stocks_filename: str):
        '''
        Constructor: creates an new instance for stock
        parameter :
        Self -- the current object 
        stocks _filename:string -- the data for the stocks 
        return None 
        '''
        #add code to raise error 
        try:
            self.stock_file = pd.read_csv(stocks_filename)
            
        except:
            raise FileNotFoundError ("file is not present")
        

        for i in range(len( stocks_filename)):
            if stocks_filename[i]== ".":
                if stocks_filename[i+1]!="c" and stocks_filename[i+2]!="s" and stocks_filename[i+3]!="v":
                    raise ValueError("please enter valid filename ")
        
                
        
    
    def rasing_error(self):
        '''
        parameter:
        self -- the current object 
        his will raise any error, this method will
        be called in all the method or that we can raise error
        '''
        whole_file = open("SQ (1).csv", 'r').readlines()
        line = whole_file[0]
        if lower.line[0]!= "date":
            raise ValueError("header is wrong ")#be more clean 
        elif lower.line[1]!= "open":
            raise ValueError("header is wrong ")
        elif lower.line[2]!= "low":
            raise ValueError("header is wrong ")
        elif lower.line[3]!= "close":
            raise ValueError("header is wrong ")
        elif lower.line[4]!= "adj close":
            raise ValueError("header is wrong ")
        elif lower.line[5]!= "volume":
            raise ValueError("header is wrong ")


    def name(self):
        max_value = self.stock_file.loc[self.stock_file['Close'].idxmax()]
        min_value = self.stock_file.loc[self.stock_file['Close'].idxmin()]
        self.stock_file["Largest percent"]= ((self.stock_file["Close"]-self.stock_file["Open"])/self.stock_file["Close"])*100
        max_percentage = self.stock_file.loc[self.stock_file['Largest percent'].idxmax()]
        min_percentage = self.stock_file.loc[self.stock_file['Largest percent'].idxmin()]
        first_list=[max_value["Close"],min_value["Close"],max_percentage["Close"],min_percentage["Close"]]
        second_list=[max_value["Date"],min_value["Close"],max_percentage["Date"],min_percentage["Date"]]
        return first_list,second_list
    
    def summary(self,start_date=None,end_date=None):
        '''
        Method:summary: gets the complete summary of stocks 
        Parameter:
        Self-- the current object:
        Returns the complete summary which will have stock price and date, where 
        it was  highest stock, lowest stock, largest moving up in a single day
        % and largest moving downward in a single day by %
        '''
        '''
        rasie error if the date given is worng or out of range 
        '''
        if start_date != None or end_date != None:
            if start_date == None:
                after_start_date = self.stock_file['Date'].max()
            elif end_date == None:
                before_end_date = self.stock_file['Date'].min()
                
            after_start_date = stock_file["Date"] >= start_date 
            before_end_date = stock_file["Date"] <= end_date
            between_two_dates = after_start_date & before_end_date
            filtered_dates = self.stock_file.loc[between_two_dates]
            
            
        value1, value2 = self.name()
            
        summary = {'summary': ["Price","Date"],'Highest High': [value1[0],value2[0]],
        'Lowest Low': [value1[1],value2[1]],
           'Largest Move Up in a single day %': [value1[2],value2[2]],
           'Largest Move Downward in a single day%': [value1[3],value2[3]],
        }
        
        df = pd.DataFrame(summary, columns = ['summary', 'Highest High','Lowest Low','Largest Move Up in a single day %','Largest Move Downward in a single day%'])
        df.style.set_properties(**{'text-align': 'center'})
        df.style.hide_index()
        df.style.format("{:.4}")
        return df
    

     def graph(self, start_date=self.start_date, end_date=self.end_date):
        '''Method -- graph
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns a line graph of the stock prices 
        '''
        pass
    
     def transform(self):
        # Eliminating columns and renaming
        self.result = self.stock_file.drop(columns=["Open", "High", "Volume", "Low", "Close"])
        self.result.columns = ['Date', 'Price']

        # Moving Average
        self.result['50-day MA'] = self.stock_file.rolling(window=50).mean()
        self.result['200-day MA'] =self.stock_file.rolling(window=200).mean()

        # Setting/formatting x, y axis and title
        self.result.Date = pd.to_datetime(self.result.Date)

    # draw plot
     def show_plot(self):
        self.result.plot(x="Date")
        plt.ylabel('Price (USD)')
        plt.title(self.input_file_name + " Stock Price: 2016 - 2021")
        plt.show()
      


    def moving_average(self):
        '''
        Method -- moving average
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns the moving average of the stocks 
        '''
        self.transform()
        self.show_plot()


    
        
    def transform_data(self,stock2_filename):
        for i in range(len( stocks2_filename)):
            if stocks_filename[i]== ".":
                if stocks_filename[i+1]!="c" and stocks_filename[i+2]!="s" and stocks_filename[i+3]!="v":
                    raise ValueError("please enter valid filename ")
       
        stock2_file = pd.read_csv(stocks2_filename)
        
        first_data = self.stocks_filename[['Date', 'Adj Close']] 
        second_data = stock2_file[['Date', 'Adj Close']]
        
        self.output1 = pd.merge(first_data, second_data, on='Date', how='inner')
        self.output1.columns=['Date', 'SQ_prize', 'PYPL_prize']

        self.output1.Date=pd.to_datetime(output1.Date)
    def stock_comparison(self):
        self.output1.plot(x="Date")
        plt.title("Closing Prices", fontsize=16)
        plt.ylabel('Price(USD)', fontsize=14)
        plt.xlabel('Year', fontsize=14)
        plt.show()
        
    def comparing_stocks(self, comparing_stock_filename):
        '''Method -- comparing_stocks 
        parameters :
        Comparing_stock_filename-- file we are going to compare with
        Returns *** need to discuss what should be returning 
        '''
        

'''

--------------------------------fix the reading second file -_____-------------------
'''
    def comparing_stocks_graph(self, comparing_stock_filename):
        '''Method -- comparing_stocks_graphs 
        Parameters 
        Self -- the current object 
        Start_date: the date which the stock price we want to see 
        end _date: the date which the stock price we want to end 
        Returns a line graph of the stock prices 
        '''
        self.transform_data(comparing_stock_filename)
        stock_comparison()
def main():
    
    value = Stocks("SQ (1).csv")
    print(value.summary())
main()   
