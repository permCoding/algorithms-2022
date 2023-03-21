import requests as req
from bs4 import BeautifulSoup
from time import sleep
import json


def get_html(sss, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    sss.headers.update(headers)
    resp = sss.get(url)
    resp.encoding = 'utf8'
    return resp.text


page = 1
host = f'https://book24.ru'
post = f'/catalog/fantastika-1649/page-{page}/'
sss = req.Session()

url = host + post
html = get_html(sss, url)
sleep(1)
soup = BeautifulSoup(html, 'lxml')
lst = soup.find_all('div', class_='product-list__item')
for elm in lst:
    cnt = elm.find('div', class_="product-card__content")
    tag = cnt.find('a', class_='product-card__name')
    href, title = host + tag['href'], tag.text
    print(href, title)
    
    # tag = elm \
    #     .find('div', class_="product-card__content") \
    #     .find('a', class_='author-list__item')
    # print(res)
    
    
    # tag = cnt.find('a', class_='author-list__item').text
    # avtor = tag.text
    # print(tag)
    
    # tag = .find('div', class_="product-card-price").find('span')
    # print(tag)
    
"""
<div class="product-card-price product-card__price">
<div class="product-card-price__current">
<span class="app-price"> 919&nbsp;₽ <!----><!----></span></div>
<div class="product-card-price__old">
<span class="app-price product-card-price__old-value"> 1&nbsp;121&nbsp;₽ </span>
<span class="product-card-price__discount"> - 18% </span></div></div>

<a href="/author/gibson-u-5546812/" class="author-list__item smartLink">
    Гибсон Уильям
</a>
<a href="/product/perekrestok-odinochestva-chast-1-6630323/" 
    class="product-card__name smartLink" 
    title="ПереКРЕСТок одиночества. Часть 1"> 
    ПереКРЕСТок одиночества. Часть 1 
</a>
"""