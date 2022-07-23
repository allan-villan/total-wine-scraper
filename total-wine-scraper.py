#!/path/to/env/bin/python3

import json
import requests
import logging
import time
import os

COOKIES = os.environ.get('MY_COOKIES')

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO)

# information for the requsts get method
cookies = COOKIES
headers = {
    'authority': 'www.totalwine.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'twm-userStoreInformation="ispStore~1121:ifcStore~1108@ifcStoreState~US-CA@method~INSTORE_PICKUP"; idm_guid=N09e218b7-cb6f-4e80-933f-d55b5816bf7a; smcLastVisitTime=1; overrideStore=true; 2022Q2_BR=variant; at_check=true; _pxhd=; 202109-MOV=false; AMCVS_F0DA403D53C3CA7B0A490D4C%40AdobeOrg=1; rrSessionId=1d026290-f3f7-11ec-a3ee-c7dea2c871ae; OptanonAlertBoxClosed=2022-06-24T20:05:23.325Z; pxcts=2a9f5f6a-f58e-11ec-8068-41614b685863; _pxvid=2a9f50be-f58e-11ec-8068-41614b685863; rcs=eF4Ny6kRgEAMAEBzil4yk__pgDYgnEDggPph_Y7leu_z0FABcouqEEkthiwwF6Tx9IpTeufawHgaqLaANAaUOibTvz0_l3sRXQ; 2022Q2_PDP=control; AMCV_F0DA403D53C3CA7B0A490D4C%40AdobeOrg=1176715910%7CMCIDTS%7C19197%7CMCMID%7C88574947807134223021057981814278352281%7CMCAID%7CNONE%7CMCOPTOUT-1658619304s%7CNONE%7CvVersion%7C5.4.0; forterToken=e35510c2bcb6440e9c0be42d56111c57_1658612103958_2727_UAL9_6; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jul+23+2022+14%3A35%3A09+GMT-0700+(Pacific+Daylight+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=150de712-21dd-4c21-985a-63412fec3bb1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=US%3BCA; mbox=PC#a8449e76d0044fc0b2a88400a8b8ac93.35_0#1721680233|session#e573df9f53f64ea2b5744b03013a81e5#1658614007',
    'if-none-match': 'W/"d566-+og5Kh6ZxYFShF2D1AV34TGGktg"',
    'referer': 'https://www.totalwine.com/wine/c/c0020?viewall=true&page=1&pageSize=120&userPrice=0-40&sort=expert-ratings&aty=1,0,0,0&instock=1',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
params = {
    'page': '1',
    'pageSize': '120',
    'state': 'US-CA',
    'shoppingMethod': 'INSTORE_PICKUP',
    'userShoppingMethod': 'INSTORE_PICKUP',
    'allStoresCount': 'true',
    'storeId': '1121',
    'price': '0-40',
    'instock': 'true',
    'batch': 'true',
    'sort': 'expert-ratings',
}

response = requests.get(
           'https://www.totalwine.com/search/api/product/categories/v2/categories/c0020/products',
            params=params, cookies=cookies, headers=headers)

data = json.loads(response.text)    

page = data['pagination']['page']
page_size = data['pagination']['pageSize']
total_pages = data['pagination']['totalPages']
total_results = data['pagination']['totalResults']

products = []
products.append(data['products'])

current_page = int(page)

wine_counter = 0
wine_counter = int(page_size)

time.sleep(2)

while page <= total_pages:
    data = None
    current_page += 1
    params['page'] = current_page

    response = requests.get(
        'https://www.totalwine.com/search/api/product/categories/v2/categories/c0020/products',
        params=params, cookies=cookies, headers=headers)

    data = json.loads(response.text) 

    products.append(data['products'])
    wine_counter += int(data['pagination']['pageSize'])

    time.sleep(2)

if wine_counter == total_results:
    print("Extracted all possible results!")