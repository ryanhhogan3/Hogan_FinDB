from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from backend.data import get_OHLC, get_option_dates, get_dividend_hist, get_portfolio, get_news, get_risk

app = Flask(__name__)

selected_ticker = "MSFT"

@app.route("/")
def home():
    return render_template('index.html', title='Welcome', username='ryan')

@app.route("/MSFT")
def msft_data():
    html_stock_data = get_OHLC(selected_ticker).to_html()
    return html_stock_data

@app.route("/options")
def msft_options():
    html_opt_data = get_option_dates(selected_ticker).to_html()
    return html_opt_data

@app.route("/dividend")
def stock_dividends():
    html_div_data = get_dividend_hist(selected_ticker).to_html()
    return html_div_data

@app.route("/portfolio")
def portfolio_page():
    html_portfolio = get_portfolio().to_html()
    return html_portfolio

@app.route("/news")
def news_page():
    html_news = get_news().to_html()
    return html_news

@app.route("/risks")
def risk_page():
    html_risks = get_risk().to_html()
    return html_risks

if __name__ == "__main__":
    app.run()