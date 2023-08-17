# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:30:22 2023

@author: Bogdan Tudose
bogdan.tudose@trainingthestreet.com
"""

#%% Before we get started
#Download Python class materials from:
        # https://marqueegroup.ca/event/inj28/
        
        #https://winpython.github.io/
                #download from Github the ~700mb zip file   
                # right click extract to unzip
            
#%% Quick test to see if code works
# import pandas as pd
# df = pd.read_csv('StockData/AAPL.csv')
# df.plot(x='Date',y='Close')

# import statsmodels.api as sm
# model = sm.OLS(df['Close'],df['Open']).fit()
# model.summary()

# C:/Users/bogda/OneDrive/Desktop/Teaching 2023/2023.08.17 - Wells Fargo - Python 1/Python Project/StockData/AAPL.csv
        #will come back to this in afternoon
#%% Section 1 - Intro to Spyder
# Running your code:
            # F9   --> runs one line (or multiple highlighted)
            # CTRL ENTER --> runs an entire section

#%% Section 2 - Data Types
x = 5 # integer
y = 2.2 #float
fName = 'Bogdan'  #string
lName = "Tudose" #string

print(fName + " " + lName)

# camelCase  --  myVariableName
# snake_case -- my_variable_name

type(x) #int --> used to check the data type

"5" + 5  #this doesn't work!
        # 10?   '55'

int("5") + 5 #10
"5" + str(5) # '55'

#%% Section 3 - Strings
greeting = "Hello World"

# Left/Right/Mid --> in excel to extract data
# in python --->  varName[x:y]

greeting[0:5] #"Hello"
        # counting starts at 0
        # 0 <= charNumber < 5
        # not including top end
 
greeting[6:8] # Wo       
greeting[-5:] # Right(text, 5), last 5 chars 
            #World


#String Methods (Formulas)
fName.upper() #'BOGDAN'
    #this doesn't modify original

fName = fName.upper()
        #this modifies original
        
messyNum = "$123,456,789"
messyNum = messyNum.strip("$").replace(",", "")
messyNum = int(messyNum)

messyNum * 2 #repeats text twice

#"-" * 100 #100 dashes
    #functions can be used with diff data types
    #methods --> only for ONE specific data type
            # text methods ---> only use them with strings

# "text".
dir("text") #directory
        
#%% Section 4 - Lists
    # like arrays in other languages
    # matrix 
    # a variable that stores multiple data
    
#inefficient
ticker1 = "AAPL"
ticker2 = "MSFT"
ticker3 = "TSLA"

#efficient
tickers = ['AAPL', 'MSFT','TSLA']
prices = [174.54, 319.33, 224.15]

#add more data
dir(tickers)
tickers.append("OPEN")
prices.append(3.32)

tickers.insert(2,'WFC')
prices.insert(2, 42.59)

# .remove("AAPL"), .pop(2)

#accessing data inside lists
tickers[-1]
prices[-1]


print(tickers[0])
prices[0]  #F9 to force a print

prices[0:2]

#%% Section 5 - Dictionaries
        #lists with named rows
        #can use "keys" to name the index
        
        # varName = {'key':value, 'key':value}
stocks = {'AAPL':174.5, 'MSFT':319.33}

#adding data - come up with a new key
stocks['MRO'] = 26

#extracting
# print(stocks['AAPL'])
stocks['AAPL'] #F9


#%% Section 6 - If Statements
    # and vs or logic
    # and --> &
    # or --> |
    # comparing 2 values--->   x == y
    # not equal to --> x != y  (vs. in Excel it's <>)


x = 50
y = 10
if x > y:
    print("x is greater than y")
    print("x is ", x)
        #code indented will only run if the condition is True
elif x == y:  #elif = else if 
    print("x is equal to y")
else: #what happens if false
    print("y is greater")
    
    
print("this is outside the if")

#%% Section 7 - Looping
    # looping allows for code to get repeated
        # analysis that you need to run x times --> you can loop it
        
        
    # two types:
        # for loop --> you know how many times to run
        # while loop --> run using a condition
      
#%%% For loop with a data set       
pricesUSD = [100, 50, 20, 15.5, 2.5]
fx = 0.80

pricesGBP = [] #creating an empty list

for x in pricesUSD:   # x = 100, x = 50        
    print(x)
    print(x * fx)
    # print("------")  
    pricesGBP.append(x * fx) #adding new price at bottom of list     
        
#%% While loop        
x = 5
while x < 100:
    print(x)
    x = x + 1
        
#%%% For loop with your own range
        # can create your own sequence/series of #s
            # range(x, y)  --> x = start, y = end
for num in range(1,50):   #  x = 1, 2, 3, .... 49
    print(num)

for num in range(100): # num = 0, 1, 2, .... 99
    print(num)

#%% Mini Assignment
        #coffee + working session until 2:15pm
        #assignment 1 try questions 1 to 5

# Will update my notes on:        
        # https://github.com/TheMarqueeGroup/WF2023











            
            
            