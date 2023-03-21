# https://www.selenium.dev/selenium/docs/api/py/
# from urllib.parse import unquote  # это при необходимости unquote('https://pcoding.ru/pdf/%D0%9A.pdf')
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from time import sleep


def get_prod(prod):
    title = prod.find_element(By.CLASS_NAME, 'catalog-product__name').text.strip()
    href = prod.find_element(By.TAG_NAME, 'a').get_attribute('href')
    price = prod.find_element(By.CLASS_NAME, 'product-buy__price').text.strip()
    try:
        stores = prod.find_element(By.CLASS_NAME, 'order-avail-wrap').text.strip()
    except:
        stores = "..."
    cols = ['title', 'href', 'price', 'stores']
    vals = [title, href, price, stores]
    return dict(zip(cols, vals))


browser = webdriver.Firefox()
page = 1
base_url, url = f'https://book24.ru/catalog', f'/fantastika-1649/page-{page}/'   
browser.get(base_url + url)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)  # браузер работает асинхронно
    
prods = browser.find_elements(By.CLASS_NAME, 'product-list__item')
for i, prod in enumerate(prods, start=1):
    price = prod.find_element(By.CLASS_NAME, 'product-card-price__current').text.strip()
    print(i, price)

browser.quit()

"""
<div data-id="product" class="catalog-product ui-button-widget "

<div class="product-buy__price">999&nbsp;₽</div>

"""