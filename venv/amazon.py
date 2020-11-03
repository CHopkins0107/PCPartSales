import requests
import config
import json

"""def urlStringCleaner(keyword:str) -> str:
    for string
"""

def amazonSearch(keyword:str) -> dict:

    url = "https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-search-by-keyword-asin"

    querystring = {"sortBy":"relevanceblender","excludeSponsored":"false","domainCode":"com","keyword":keyword,"page":"1"}

    headers = {
        'x-rapidapi-host': "axesso-axesso-amazon-data-service-v1.p.rapidapi.com",
        'x-rapidapi-key': config.amazon
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json()['searchProductDetails'][0])
    return response.json()['searchProductDetails'][0]['price']

def walmartSearch(keyword:str) -> dict:

    url = "https://axesso-walmart-data-service.p.rapidapi.com/wlm/walmart-search-by-keyword"

    querystring = {"sortBy": "best_match", "page": "1", "keyword": keyword, "type": "text"}

    headers = {
        'x-rapidapi-host': "axesso-walmart-data-service.p.rapidapi.com",
        'x-rapidapi-key': config.walmart
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    product_url = "walmart.com/" + response.json()['numberOfProducts'][0]

    url2 = "https://axesso-walmart-data-service.p.rapidapi.com/wlm/walmart-lookup-product"

    querystring2 = {
        "url": "https%3A%2F%2Fwww.walmart.com%2Fip%2FOculus-Quest-2-Advanced-All-In-One-Virtual-Reality-Headset-64-GB%2F484166583"}

    headers2 = {
        'x-rapidapi-host': "axesso-walmart-data-service.p.rapidapi.com",
        'x-rapidapi-key': "5a22100f37msh7f23b32d700f3d7p16cd86jsn67876212964e"
    }

    response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

    print(response.text)
    return