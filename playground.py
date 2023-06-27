import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import yahooquery as yq
import numpy as np

#import data_cleaning

#nvda = yf.Ticker("NVDA")
#print(nvda.info.keys())

# interesting attributes
#'longBusinessSummary'
#'marketCap'
#''


# today = date.today()
# yesterday = today - timedelta(days = 7)


# data = yf.download('NVDA', start= str(yesterday), end=str(today))

#print(data)

# 1. find the right tickers 
    # a. take top 500 tech stocks 
    # b. download descriptions 
    # c. keep stocks with AI ML related keywords  
# 2. download their data 
# 3. display, ticker, market cap 

def extract_quotes(screener_output): 
    output = []
    for screener in screener_output.keys(): 
        s = np.array(screener)
        print(s)
        #print(screener.get('quotes').get('symbol'))
    

techSceener = yq.Screener() 

data = pd.DataFrame(techSceener.get_screeners(['information_technology_services', 'most_visited_technology', 'ms_technology']))


#print(type(data))
#print(data.keys())

#data_cleaning.extract_quotes(data)

