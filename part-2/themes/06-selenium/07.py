# https://www.selenium.dev/selenium/docs/api/py/
# from urllib.parse import unquote  # это при необходимости unquote('https://pcoding.ru/pdf/%D0%9A.pdf')
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from time import sleep


browser = webdriver.Firefox()
base_url, url = 'https://www.dns-shop.ru', '/catalog/8a9ddfba20724e77/ssd-nakopiteli/'

cols = ['id', 'title', 'href', 'price', 'stores']
i, lst, count = 0, [], 3
for page in range(1, count+1):
    print(f'page={page}')
    post = f'?stock=now-today&p={page}'
    browser.get(base_url + url + post)
    
    sleep(3)
    prods = browser.find_elements(By.CLASS_NAME, 'catalog-product')
    
    for prod in prods:
        title = prod.find_element(By.CLASS_NAME, 'catalog-product__name').text.strip()
        href = prod.find_element(By.TAG_NAME, 'a').get_attribute('href')
        price = prod.find_element(By.CLASS_NAME, 'product-buy').text.strip().split('\n')[0]
        stores = prod.find_element(By.CLASS_NAME, 'order-avail-wrap').text.strip()
        i += 1
        vals = [i, title, href, price, stores]
        lst.append(dict(zip(cols, vals)))

with open('prods.json', 'w', encoding='utf8') as f:
    json.dump(lst, f, ensure_ascii=False, indent=4)

browser.quit()

"""
<div data-id="product" class="catalog-product ui-button-widget "

<div class="product-buy__price">999&nbsp;₽</div>

"""