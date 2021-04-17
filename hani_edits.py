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
        for i in range(len( stocks_filename)):
            if stocks_filename[i]== ".":
                if stocks_filename[i+1]!="c" and stocks_filename[i+2]!="s" and 
                stocks_filename[i+3]!="v:
                raise ValueError("please enter valid filename ")
                

        try:
            self.stock_file = pd.read_csv(stocks_filename)
            self.major_index = pd.read_csv(major_index)
        except:
            raise FileNotFoundError ("file is not present")

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



    def summary(self):
        '''
        Method:summary: gets the complete summary of stocks 
        Parameter:
        Self-- the current object:
        Returns the complete summary which will have stock price and date, where 
        it was  highest stock, lowest stock, largest moving up in a single day
        % and largest moving downward in a single day by %
        '''
        max_value = self.stock_file.loc[self.stock_file['Close'].idxmax()]
        min_value = self.stock_file.loc[self.stock_file['Close'].idxmin()]
        self.stock_file["Largest percent"]= ((self.stock_file["Close"]-self.stock_file["Open"])/self.stock_file["Close"])*100
        max_percentage = self.stock_file.loc[self.stock_file['Largest percent'].idxmax()]
        min_percentage = self.stock_file.loc[self.stock_file['Largest percent'].idxmin()]
        
        summary = {'summary': ["Price","Date"],'Highest High': [max_value["Close"],max_value["Date"]],
        'Lowest Low': [min_value["Close"],min_value["Date"]],
           'Largest Move Up in a single day %': [max_percentage["Largest percent"],max_percentage["Date"]],
           'Largest Move Downward in a single day%': [min_percentage["Largest percent"],min_percentage["Date"]],
        }
        
        df = pd.DataFrame(summary, columns = ['summary', 'Highest High','Lowest Low','Largest Move Up in a single day %','Largest Move Downward in a single day%'])
        
        return df
        
    
    
       

def main():
    
    value = Stocks("SQ (1).csv","asd")
    print(value.summary())
    
main()
