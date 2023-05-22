import yfinance as yf
import pandas as pd
import datetime as dt

def get_OHLC(ticker):
    stockobj = yf.Ticker(ticker)
    OHLCV = pd.DataFrame(stockobj.history('1y'))
    return OHLCV

def get_option_dates(ticker):
    stockobj = yf.Ticker(ticker)
    option_dates = pd.DataFrame(stockobj.options)
    return option_dates

def get_dividend_hist(ticker):
    stockobj = yf.Ticker(ticker)
    div_hist = pd.DataFrame(stockobj.dividends)
    return div_hist

def get_portfolio():
    csv_data = pd.read_csv('CSV_maker - Sheet1.csv')
    csv_data1 = pd.DataFrame(csv_data)
    return csv_data1

def get_news():
    news_data = pd.read_csv("https://raw.githubusercontent.com/suraj-deshmukh/BBC-Dataset-News-Classification/master/dataset/dataset.csv", encoding="ISO-8859-1")
    return news_data

def get_risk():
    risk_data = pd.read_csv("https://raw.githubusercontent.com/GFDRR/open-risk-data-dashboard/master/backend/contents/countries/country_groups.csv")
    return risk_data

def get_todays_date():
    today = dt.datetime.today()
    return today

# def callPyTime():
#     time= dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # print(time)
#     return time
