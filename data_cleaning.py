import pandas as pd 
import re 
import packed_bubbles

ai_keywords = ["artificial intellege","machine learning", "\sml\s|\.", "\sai\s|\." ]

def find_tickers(raw_data): 
    tickers = []
    
    for screener in raw_data.keys(): 
        # Find the quotes in each screener
        quotes = list(raw_data[screener]["quotes"])
        
        for q in quotes:
            #Extract only the tickers of each symbol  
            tickers.append(q["symbol"])
    
    #Return a list of distinct tickers 
    return list(set(tickers))

def get_ticker_descrition(TickerObj): 
    
    Symbol = []
    Description = []
    
    # Go through all tickers 
    for t in TickerObj.tickers.keys(): 
        Symbol.append(t)
        # Extract the business summary 
        Description.append(TickerObj.tickers[t].info['longBusinessSummary'])
    
    results_dict = {"Symbol": Symbol, "Description": Description}
    
    # Return as a data frame
    return pd.DataFrame.from_dict(results_dict)

def replace_punct(s): 
    punct = r"[!\"#\$%&\'\(\)\*\+,\./:;<=>\?@\[\\\]\^_`{\|}~]"
    return re.sub(punct, " ", s)


def mentions_ai(description, keyword_list = ai_keywords): 
    # remove punctuation
    d = replace_punct(description)
    
    # combine keywords 
    combined = "(" + ")|(".join(keyword_list) + ")" 
    
    # search for keywords 
    if re.search(combined, d, re.IGNORECASE):
        return True
    else: 
        return False 
    

def get_market_cap(ticker, TickerObj): 
    return TickerObj.tickers[ticker].info['marketCap']