**Stock Analysis and Visualization**

**Description:**
The Stock Analysis and Visualization package would be the first step for the investor who is conducting an initial search of a large range of publicly traded companies that fit his or her investment goal.

**Purpose:**
The purpose of this package is to provide the user with basic equity performance statistics and a graphical representation of a user selected publicly traded company’s share price over time. Over the past 10 years python has made its mark in the financial markets and has streamlined how data is shaping the investment decisions of many savvy investors. There are many modules and packages that are like what we have developed for this project. We believe in this crowded space there is a need for a simple package that supplies the facts and provides insight for the financial decision maker which is what we believe our package delivers.

**Data:** User downloads the selected company historical share price data from Yahoo finance

**Language Used:** Python

**Libraries Used:** Numpy, Pandas and  Matplotlib

T**he organization of the package code in the repository:**

1.	SQ.csv: Data for Square collected from Yahoo Finance for for dates 05-04-16 to 01-04-21
2.	PYPL.csv: Data for PayPal collected from Yahoo Finance for for dates 05-04-16 to 01-04-21. Will be used for comparing stocks.
3.	Modules: Modules ending in “.py” containing Python code defining classes and functions. 

      Outline of our code:
      
       Summary Table: The summary table will include a brief outline of the company's stock performance: when the                  company's stock price hit its highest high and its lowest low for the period, and the largest percentage change up and down during the time frame with the associated dates.
       
       Graphs: The graph will be a line graph to help visualize the company’s stock performance for the chosen period.
       
       Moving average: The moving average is a layered feature on the graph which will be limited to the 50- and 200-day moving average for the company’s stock. For many investors these moving average provide technical indicators of the stock rising or falling.  
       
       Comparing stocks summary with accompanying graph: If the user decides to input two different publicly traded company stocks the table and graph will reflect the above information for both companies which will give the user a side-by-side comparison of the two companies.

4.	Test: Test scripts ending in “.py” containing unit tests covering most of the package’s functionality. (add the kind of test cases)

5.	__init__.py: Initialization script marking the repository as a Python package. 

**Examples of usage**

This package can be used by the novice or more advanced financial investor. Once the code runs the user is presented with a graph that provides a graphical representation of the company’s performance with the accompanying 50 and 200-day moving averages.
Also provided is a summary table that is an overview of the investment performance during the time period. The combination of these two outputs will provide the investor a tangle idea of the highest high, lowest low, and overall equity performance of the company. To provide the user with as much information as possible we have provided a comparison table that contains the target companies stock performance data as well as its closest competitors. With these outputs we believe that the investor would be informed enough to make an investment decision to buy or sell the company’s stock.

**Running the code**

Please refer to Result.ipynb to see the outputs. If you want to use results.py file, please mark df.style in Summary and Comparing_summary methods as comments and return df. 
Panas support df.style only in Jupyter Notebook as of now.


**Report of the project**

See the full report and code of this project here for further reference

