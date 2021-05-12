# -*- coding: utf-8 -*-
import requests
import json


def BtcBrl():

    url = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
    try:
        price_request = requests.get(url)    
        price_request= price_request.json()
        price = float(price_request['BTCBRL']['ask'])

        with open('last_price.txt','w') as p:
            p.write(str(price))

        get_test = True

    except:
        print(price_status)
        with open('last_price.txt','r') as p:
            price = p.read()

        get_test = False

    return price, get_test

def Real2Sats(price):
    return 1e8*(1.0/price)


def composer():

    price_tuple = BtcBrl()
    price = Real2Sats(price_tuple[0])
    price_str = str(round(price,2)).replace('.',',')

    if price_tuple[1]:
        post = "R$1,00 vale {} satoshis.".format(price_str)
    else:
        post = "Na última vez que olhei, R$1,00 valia {} satoshis.".format(price_str)

    return post



