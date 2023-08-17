# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:51:57 2023

@author: Bogdan Tudose
"""

#%% Pandas Package
import pandas as pd
sp500 = pd.read_csv('StockData/SP500.csv')
finDeals = pd.read_excel('ExData/Data Manipulation Worksheet.xlsx')
        #right click, copy Relative Path, to quickly grab link 
        
#%% Moving Averages
sp500['5-day MA'] = sp500['Close'].rolling(5).mean()
sp500['20-day MA'] = sp500['Close'].rolling(20).mean()

days = [5, 20, 15, 100, 200, 250, 300, 45, 90]
for x in days:
    sp500[ str(x) +'-day MA'] = sp500['Close'].rolling(x).mean()

sp500.plot(x='Date', y=['Close','20-day MA','250-day MA'])
sp500.to_excel('Output/sp500 with averages.xlsx')

#%% Calculations
sp500['Intraday Return'] = sp500['Close'] / sp500['Open'] - 1
        # close / open - 1 = (close-open) / open
sp500['Daily Return'] = sp500['Close'] / sp500['Close'].shift(1) - 1
        #  close today / close yesterday - 1
        
sp500['Returns'] = sp500['Close'].pct_change() #same as line above
        # assumes that dates are sorted in ascending order (old-->new)

#%% Explore/Check Data for Cleaning
    # .info() ---> info about the columns
finDeals.info()
    # numbers should be float or int
    # dates should be datetime
    # SIZE --> should be float
sp500.info()

finDeals = pd.read_excel('ExData/Data Manipulation Worksheet.xlsx',
                         sheet_name=1)
                            # sheet_name="Financing Table Clean"

# finDeals = pd.read_excel('ExData/Data Manipulation Worksheet.xlsx',
                         # skipfooter=11)

sp500 = pd.read_csv('StockData/SP500.csv', parse_dates=['Date'])
aapl = pd.read_csv('StockData/AAPL.csv', parse_dates=['Date'], index_col=['Date'])

#%% Accessing Data
        #   dataSet.loc[row][col header]  # loc = location (your new index)
        #   dataSet.iloc[row][col header]  # iloc = integer location (row #s)
aapl.loc['2016-02-23']['Close']
# aapl.iloc[6]['Close']
sp500.iloc[0:5] #first 5 rows
aapl.loc['2016'] #all the 2016 data

q1 = aapl.loc['2015-01':'2015-03'] #new table
q1.to_excel('Output/q1 2015 apple.xlsx')

#%% Plot just 2014
aapl.loc['2014']['Close'].plot()

finDeals.iloc[0:5]

#%% Filtering with Pandas
            #  table[conditions]
            #and ---> &
            #or ---> |
        
        #deals bw 200 and 800
condition1 = finDeals['SIZE'] >= 200
condition2 = finDeals['SIZE'] <= 800
filter1 = finDeals[condition1  & condition2]

filter2 = finDeals[finDeals['SIZE'].between(200,800)]

#Find all the deals done by 
    #Salomon Smith Barney
    #Lehman Brothers
c1 = finDeals['LEAD UNDERWRITER'] == "Salomon Smith Barney"
c2 = finDeals['LEAD UNDERWRITER'] == "Lehman Brothers"
filterBanks = finDeals[c1 | c2]


#one line
filterBanks = finDeals[  (finDeals['LEAD UNDERWRITER'] == "Salomon Smith Barney") |
                       (finDeals['LEAD UNDERWRITER'] == "Lehman Brothers")]

#%% Mini Pandas Assignment
        # jot down how many rows in each filter

#Production/miniPandasAssignmentQuestions.py
#1) Load Apple data set (StockData --> aapl.csv) 
    #and Financing Deals data set (ExData --> Data Manip --> Clean tab)

#2) Find all the days of Apple where closing share price was between 70 and 75
    
#3) Financing Deals data (Data Manip file) --> find all deals done by GS and JPM

#4) Find all the deals done in May of 2006
#5) Find all the deals done by Merrill Lynch in Real Estate
#6) Calculate the returns of Apple's closing share price
    #what is the average return and standard deviation?







