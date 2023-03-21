import requests as req
from bs4 import BeautifulSoup
from time import sleep
import json
import re


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    resp = req.get(url, headers=headers)
    resp.encoding = 'utf8'
    return resp.text

# https://book24.ru/catalog/page-2/fantastika-1649/?by=desc&sort=date
page = 1
host = f'https://book24.ru/catalog'
post = f'/fantastika-1649/page-{page}/'

url = host + post
html = get_html(url)
sleep(1)
soup = BeautifulSoup(html, 'lxml')
lst = soup.find('div', class_='product-list').prettify()
with open('book24.html', 'w', encoding='utf8') as f:
    print(lst, file=f)
