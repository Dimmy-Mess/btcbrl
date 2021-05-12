# -*- coding: utf-8 -*-
import requests
import json
import time

def BtcBrl():

    url = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
    try:
        price_request = requests.get(url)    
        price_request= price_request.json()
        price = float(price_request['BTCBRL']['ask'])
        data = price_request['BTCBRL']['timestamp']
        with open('last_price.txt','w') as p:
            p.write(str(price))

        get_test = True

    except:
        print(price_status)
        with open('last_price.txt','r') as p:
            price = p.read()

        get_test = False

    return price, get_test,data

def Real2Sats(price):
    return 1e8*(1.0/price)

def organize_data(timestamp):
    n_month = {'Jan': '01', 'Feb': '02', 'Mar':'03','Apr':'04','May':'05','Jun': '06',
    'Jul': '07', 'Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    moment = time.ctime(int(timestamp)).split()

    return f"{moment[2]}/{n_month[moment[1]]}/{moment[-1]}, às {moment[-2]}:"

def composer():

    price_tuple = BtcBrl()
    price = Real2Sats(price_tuple[0])
    price_str = str(round(price,2)).replace('.',',')
    data = organize_data(price_tuple[2])
    if price_tuple[1]:
        post = "{} R$1,00 vale {} satoshis.".format(data, price_str)
    else:
        post = "Na última vez que olhei, R$1,00 valia {} satoshis.".format(price_str)

    return post
