from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from backend.data import *
from getTime import callPyTime

app = Flask(__name__)



selected_ticker = "MSFT"

@app.route("/")
def home():

    return render_template('index.html', time=format(dt.datetime.strftime(dt.datetime.now(), "%d %B %Y %X")))

@app.route("/MSFT")
def msft_data():
    html_stock_data = get_OHLC(selected_ticker)
    return render_template('contentWIP.html', tables=[html_stock_data.to_html()], titles=[''])

@app.route("/options")
def msft_options():
    html_opt_data = get_option_dates(selected_ticker)
    return render_template('contentWIP.html', tables=[html_opt_data.to_html()], titles=[''])


@app.route("/dividend")
def stock_dividends():
    html_div_data = get_dividend_hist(selected_ticker)
    return render_template('contentWIP.html', tables=[html_div_data.to_html()], titles=[''])

@app.route("/portfolio")
def portfolio_page():
    html_portfolio = get_portfolio()
    return render_template('contentWIP.html', tables=[html_portfolio.to_html()], titles=[''])

@app.route("/news")
def news_page():
    html_news = get_news()
    return render_template('contentWIP.html', tables=[html_news.to_html()], titles=[''])

@app.route("/risks")
def risk_page():
    html_risks = get_risk()
    return render_template('contentWIP.html', tables=[html_risks.to_html()], titles=[''])

@app.route("/time")
def getTime():
    return callPyTime()



if __name__ == "__main__":
    app.run(app, debug=True)