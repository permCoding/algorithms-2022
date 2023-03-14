from bs4 import BeautifulSoup
import re
import requests


# def get_html(fn):
#     with open(fn, 'r', encoding='utf8') as f:
#         return f.read()


def get_html(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    resp = requests.get(url, headers=head)
    resp.encoding = "utf8"
    return resp.text


# filename = './html/index_a.html'
# html = get_html(filename)

url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)
# print(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup.find_all('title'))
# print(soup.find('title'))
# print(soup.find('title').text)

# print(soup.find_all(class_='title'))

# for e in soup.find_all('span'): print(e)
# for e in soup.find_all('span'): print(e.text)
# = = = = = = = = = = = = = = = 

# prod = soup.find('div', class_='prod__info')
prod = soup.find('div', { 'class': 'prod__info' })
prodname = prod.find('div', id='prodname').text.strip()
print(prodname)

# prodname = prod.find('div', {'id':'prodname', 'class':'prod__name'}).text.strip()
# prodprice = prod.find_all('div')[1].find_all('span')[1].text
# print(f"{prodname} | {prodprice}")

# pp = prod.find_all('div')[1].find_all('span')
# for e in pp: print(e.text)
# for i in range(len(pp)-1,-1,-1): print(pp[i].text)
# = = = = = = = = = = = = = = = 

# find_price = soup.find('span', string="Стоимость:")
# print(find_price)
# print(find_price.find_next_sibling())
# for e in find_price.find_next_siblings('span'):
#     print('-', e)

# find_price = soup.find('span', string=re.compile('Руб\.?', re.I))
# find_price = soup.find('span', string=re.compile('[Рр]уб\.{0,1}'))
# print(find_price)
# print(find_price.find_previous_sibling())
# print(find_price.find_previous_sibling().text)
# for e in find_price.find_previous_siblings('span')[::-1]:
#     print('+', e.text)
# = = = = = = = = = = = = = = = 
# links = soup.find(class_="shops__info").find_all("a")
# for link in links:
#     print(link.get("href"))
#     print(link["href"])
#     print(link.text)
# = = = = = = = = = = = = = = = 
# def class_without_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# tags = soup \
#     .find('div', class_='prod__info') \
#     .find_all(class_without_id)[:2]
# for e in tags: print(e)
# = = = = = = = = = = = = = = = 
