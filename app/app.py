from flask import Flask, render_template, redirect, url_for, jsonify
import yfinance as yf
import pandas as pd
from backend.data import *
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from getTime import callPyTime
from flask import request
import secrets

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


selected_ticker = "MSFT"

@app.route("/")
def home():
    q = request.args.get('query')
    if q:
        try:
            print(q)
            html_stock_data = get_OHLC(q)
            return render_template('stockSearch.html', stock_search=q, last_price=getLastPrice(q), tables=[html_stock_data
                                                                                                           .to_html()], titles=[''])
        except:
            print("nothing submited")
            return render_template('index.html', time=format(dt.datetime.strftime(dt.datetime.now(), "%d %B %Y %X")))
    else:
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
    
    return 'portfolio page'

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

@app.route("/data/<ticker>")
def getJSONdata(ticker):
    history = get_OHLC(ticker)['Close']
    return jsonify(history.to_json(orient='records'))

@app.route("/search")
def searchBar():
    q = request.args.get('query')
    if q:
        try:
            print(q)
            html_stock_data = get_OHLC(q)
            return render_template('stockSearch.html', stock_search=q, last_price=getLastPrice(q), tables=[html_stock_data.to_html()], titles=[''])
        except:
           
            print("nothing submited")
            return render_template('searchBar.html')
    else:
        print("nothing submited")
        return render_template('searchBar.html')


if __name__ == "__main__":
    app.run(app, debug=True)