import json
import requests
from bs4 import BeautifulSoup


LIST_URL = 'http://api.exchangeratesapi.io/v1/latest?access_key=18f3ee7f7ff2c8f89f9240cde7f54dd9&symbols=USD,KGS,RUB'


def get_currency_list():
    list_ = requests.get(LIST_URL).text
    soup = BeautifulSoup(list_, 'lxml').p.string
    dict_ = json.loads(soup)
    message = str()
    for currency, value in dict_['rates'].items():
        value = round(value, 2)
        message += f'{currency} : {value}\n'
    return message


def convert(amount, currency1, currency2):
    # EXCHANGE_URL = f'https://api.exchangeratesapi.io/v1/convert?access_key=18f3ee7f7ff2c8f89f9240cde7f54dd9&from={currency1}&to={currency2}&amount={amount}'
    EXCHANGE_URL = f'https://api.exchangeratesapi.io/v1/convert?access_key=18f3ee7f7ff2c8f89f9240cde7f54dd9&from=USD&to=KGS&amount=10'

    a = requests.get(EXCHANGE_URL).text
    print(a)


convert(12, 22, 4)