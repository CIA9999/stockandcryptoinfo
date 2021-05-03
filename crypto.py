import matplotlib.pyplot as plt
import requests
import yfinance as yf
from bs4 import BeautifulSoup
import os
import pandas as pd
import pandas_datareader


command = input("What command would you like to execute: ")


if command == "live price":
    ticker222 = input("What stock would you like to get the current price on: ")
    alert = input("Would you like to set a price alert if so enter it now: ")
    url = 'https://ca.finance.yahoo.com/quote/' + ticker222 + "-USD" + '?p=' + ticker222 + "-USD" + '&.tsrc=fin-srch'
    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        price = soup.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
        print(price)
        os.system('clear')
        if price == alert:
            print("Your stock has hit it price target")

if command == "price":
    ticker234 = input("What stock would you like to get the current price on: ")
    url = 'https://ca.finance.yahoo.com/quote/' + ticker234 + "-USD" + '?p=' + ticker234 + "-USD" + '&.tsrc=fin-srch'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    print(price)


if command == "chart":
    ticker = input("What ticker/tickers would you like to graph: ")
    ticker_list = ticker.split()
    sd = input("What would you like the start date to be: ")
    ed = input("What would you like the end date to be: ")
    data = yf.download(ticker_list, sd, ed)
    data.Close.plot()
    plt.show()