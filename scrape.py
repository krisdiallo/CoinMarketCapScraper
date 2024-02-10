#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:37:45 2018
@author: kogito
"""
import csv
import re
import string
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt
from datetime import timedelta

currency_list_url = "https://coinmarketcap.com"

class Scraper():
      
    
    @classmethod
    def get_cryptos(self, pages):
        crypto_list = []
        for p in range(pages):
            page_url = currency_list_url + f"/?page={p+1}"
            r = requests.get(page_url)
            soup = BeautifulSoup(r.text, 'lxml')
            table = soup.find('table')
            for row in table.find_all('tr'):
                crypto_name = row.find('a', {"class": "cmc-link"})
                if crypto_name:
                    crypto_name = crypto_name.attrs.get("href")
                    crypto_list.append(crypto_name)
        return crypto_list
            
            
                
    @classmethod
    def get_historical_data(self, coin_url, start_date=dt.now() - timedelta(365)):
        coin = coin_url.split("/")[-2].upper()
        print(start_date)
        url = currency_list_url + coin_url + "historical-data"
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        browser.set_window_size(1440, 900)
        browser.get(url)
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            try:
                xpath_expression = "//button[contains(@class, 'sc-2861d03b-0') and text()='Load More']"
                load_more_button = WebDriverWait(browser, 1).until(
                    EC.visibility_of_element_located((By.XPATH, xpath_expression))
                )
                if load_more_button.is_displayed():
                    load_more_button.click()
                else:
                    break

                html = browser.page_source
                soup = BeautifulSoup(html, features="html.parser")
                table = soup.find('table')
                rows = table.find_all('tr')
                last_row = rows[-1]
                last_date = last_row.findChildren('td')[0].string

                if dt.strptime(last_date, "%b %d, %Y") <= start_date:
                    print(f"{last_date} is earlier than {start_date}")
                    break

            except EC.NoSuchElementException:
                break
            except Exception as e:
                print("An error occurred:", e)
                break
        print(f"finishing execution of {coin}")     
        data = []
        html = browser.page_source
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find('table')
        for row in table.find_all('tr'):
            cells = row.findChildren('td')
            values = []
            for cell in cells:
                value = cell.string
                values.append(value)
            try:
                Date = values[0]
                Open = values[1]
                High = values[2]
                Low =  values[3]
                Close = values[4]
                Volume = values[5]
                MarketCap = values[6]
            except IndexError:
                continue
            data.append([Date, coin, Open, High, Low, Close, Volume, MarketCap])
        # for item in data:
        #     print(item)
        browser.quit()
        return data

    @classmethod
    def write_to_csv(self, data, crypto):
        f = open(f'{crypto}_1d.csv', 'w')
        with f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow(['Date', 'Coin', 'Open', 'High', 'Low', 'Close', 'Volume', 'MarketCap'])

            for row in data:
                writer.writerow(row)
