import finnhub
from decouple import config

finnhub_client = finnhub.Client(api_key=config("API_KEY"))


def get_stock_price_info(stock):
    return finnhub_client.quote(stock)


def get_current_stock_price(stock):
    return finnhub_client.quote(stock)['c']


def get_high_price_of_the_day(stock):
    return finnhub_client.quote(stock)['h']


def get_low_price_of_the_day(stock):
    return finnhub_client.quote(stock)['l']


def get_open_price_of_the_day(stock):
    return finnhub_client.quote(stock)['o']


def get_previous_close_price(stock):
    return finnhub_client.quote(stock)['pc']
