import yfinance as yf
import pandas as pd
from .models import yahoo
import json
import random
import time
def yahoo_historyy(ticker_name, ticker_object):
    acceptable_columns = ['ticker', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
    ticker_name = ticker_name.upper()
    try:
        df_yahoo_history = ticker_object.history(period='max',threads = False)
        if not "ticker" in df_yahoo_history.columns:

            df_yahoo_history.insert(0, "ticker", ticker_name)
        for column in df_yahoo_history.columns:

            if column not in acceptable_columns:
                df_yahoo_history.drop([column], axis=1, inplace=True)

        for index in acceptable_columns:

            if index not in df_yahoo_history.columns:

                df_yahoo_history.insert(acceptable_columns.index(index), index, ' ')
        df_yahoo_history.index.name = "date"
        df_yahoo_history = df_yahoo_history.reset_index()
    except Exception as e:
        print(e)
        return pd.DataFrame()
    df_yahoo_history.rename(columns={'Stock Splits':'StockSplits'}, inplace=True)

    return df_yahoo_history

def yahoo_history_data_insert():
    ticker_object = yf.Ticker('AAPL')
    df = yahoo_historyy('AAPL',ticker_object)
    df['date']=df['date'].astype('str')
    df.drop('ticker',1,inplace=True)
    df = df.to_dict()
    print(len(df['date']))
    tics = ['BAC','T','OEDV','7SEA','GOOG']
    for i in range(100000):
        for j in range(len(df['date'])):
            t = tics[random.randint(0, 4)]
            #print(t)
            obj = yahoo.objects.all()
            a =yahoo.objects.create(ticker = t,date=df['date'][j], Open=df['Open'][j], High=df['High'][j],Low=df['Low'][j],Close=df['Close'][j],Volume=df['Volume'][j],Dividends=df['Dividends'][j],StockSplits=df['StockSplits'][j])
            a.save()
            