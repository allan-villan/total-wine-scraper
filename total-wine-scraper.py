#!/path/to/env/bin/python3

import json
import requests
import logging
import time
import os

COOKIES = os.environ.get('MY_COOKIES')
HEADERS = os.environ.get('MY_HEADERS')

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO)

# information for the requsts get method
cookies = COOKIES
headers = HEADERS
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

    try:
        response.status_code != 200
    except:
        logging.INFO("Something wrong with GET request...")

    data = json.loads(response.text) 

    products.append(data['products'])
    wine_counter += int(data['pagination']['pageSize'])

    time.sleep(2)

if wine_counter == total_results:
    print("Extracted all possible results!")