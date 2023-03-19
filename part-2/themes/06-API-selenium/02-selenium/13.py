# https://www.selenium.dev/selenium/docs/api/py/
# from urllib.parse import unquote  # это при необходимости unquote('https://pcoding.ru/pdf/%D0%9A.pdf')
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_data():
    lst_page = []
    lst = browser.find_elements(By.CLASS_NAME, 'list-entry')
    for elm in lst:
        title = elm.find_element(By.TAG_NAME, 'h5').text.strip()
        lst_page.append(title)
    return lst_page


count_pages = 3
news = []

browser = webdriver.Firefox()
browser.get('https://pgatu.ru/today/')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
news.extend(get_data())

for _ in range(count_pages-1):
    btn_next = browser.find_element(By.CLASS_NAME, 'next')
    btn_next.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    news.extend(get_data())

for elm in news: print(elm)

browser.quit()

"""
<nav id="pagination">
<div class="pagination">
<span class="current prev">Предыдущая</span>
<span class="current">1</span>
<a href="#">2</a>
<a href="#">3</a>
<a href="#">4</a>
<a href="#">5</a>
<a href="#">6</a>
<a href="#">7</a><a href="#">8</a><a href="#">9</a><a href="#">10</a><span>...</span>
<a href="#" class="ep">208</a>
<a href="#" class="next">Следующая</a></div></nav>

"""