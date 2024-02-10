# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:05:35 2017
@author: SuperKogito
"""
from gui import MainWindow
from scrape import Scraper

def main():
    #MainWindow('Scraper')
    scraper = Scraper()
    list_of_cryptos = scraper.get_cryptos(1)
    for coin in list_of_cryptos:
        data = scraper.process(coin)
        scraper.write_to_csv(data, coin.split("/")[-2].upper())
if __name__ == '__main__':
    main()
