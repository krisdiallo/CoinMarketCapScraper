# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:05:35 2017
@author: SuperKogito
"""
from gui import MainWindow
from scrape import Scraper
import sys
from datetime import datetime as dt


def validate_date_arg(date_arg):
    try:
        date = dt.strptime(date_arg, "%Y-%m-%d")
        return date
    except:
        raise ValueError("Date must be of format YYYY-MM-DD")

def main(pages, start_date):
    print(pages, start_date)
    #MainWindow('Scraper')
    scraper = Scraper()
    list_of_cryptos = scraper.get_cryptos(pages)
    for coin in list_of_cryptos:
        data = scraper.get_historical_data(coin, start_date)
        scraper.write_to_csv(data, coin.split("/")[-2].upper())
        
        
    #test individual coin by name
    # coin = "/currencies/FIRST-DIGITAL-USD/"
    # data = scraper.get_historical_data(coin, start_date)
    # scraper.write_to_csv(data, coin.split("/")[-2].upper())
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: script.py [number of pages] [date in YYYY-MM-DD format]")
        sys.exit(1)
    number_arg = sys.argv[1]
    date_arg = sys.argv[2]
    try:
        number = int(number_arg)
    except ValueError:
        print("First argument must be a number.")
        sys.exit(1)
    try:
        start_date = validate_date_arg(date_arg)
    except ValueError as e:
        print(e)
        sys.exit(1)
    main(number, start_date)
