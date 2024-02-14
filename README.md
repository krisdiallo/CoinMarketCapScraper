# CoinMarketCapScraper
a lightweight python scraper to get/scrape historical data from the CoinMarketCap website and convert it into a csv file. This is an initial step for a data mining process to develop a predictive model of cryptocurrencies prices. This code is built with python 3.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
In order to excute this code you will need the following python 3 packages:
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) module
```
sudo pip install beautifulsoup4
```
* [requests](https://docs.python-requests.org/en/master/) module
```
sudo pip install requests
```
* [selenium](https://pypi.org/project/selenium/) module
```
sudo pip install selenium
```

## Running
This code can be either excuted using a python IDE or by running the following command in the terminal:
```
python3 main.py [pages] [start_date]
```
`pages` is the arg for how many pages of crypto from coinmarketcap.com to capture (increments of 100 cryptos)

`start_date` is the arg for how far back you want the historical data for a the cryptos captured in `(YYYY-MM-DD)` format (the historical data will go slightly further back than start date)


## Contributing
If you have any improvement suggestions, please contact me.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* The nameless heros of Stackoverflow
