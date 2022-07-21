#!/path/to/env/bin/python3

import json
import requests
import logging
import info

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO)

# information for the requsts get method
cookies = info.cookies
headers = info.headers
params = info.params

response = requests.get(
           'https://www.totalwine.com/search/api/product/categories/v2/categories/c0020/products',
            params=params, cookies=cookies, headers=headers)

try:
    response.status_code == 200
except:
    logging.info('API call failed. Response received: ' + response.status_code)
else:
    data = json.loads(response.text)    

    page = int(data['pagination']['page'])
    page_size = int(data['pagination']['pageSize'])
    total_pages = int(data['pagination']['totalPages'])
    total_results = int(data['pagination']['totalResults'])

    products = []
    products.append(data['products'])

    while page < total_pages:
        page += 1
        params['page'] = page

        response = requests.get(
            'https://www.totalwine.com/search/api/product/categories/v2/categories/c0020/products',
                params=params, cookies=cookies, headers=headers)

        products.append(data['products'])
        
    print(json.dumps(products, indent=4, sort_keys=True))