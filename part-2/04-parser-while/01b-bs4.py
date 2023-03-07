import requests
from bs4 import BeautifulSoup


def get_html(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    resp = requests.get(url, headers=head)
    resp.encoding = "utf8"
    return resp.text


url = 'https://pcoding.ru/darkNet.php'
html = get_html(url)

soup = BeautifulSoup(html, 'html.parser')
print(soup.title.text)

links = soup.find_all('a', class_='links')
for link in links:
    if '.pdf' in link.text:
        print(link.text, link['href'])

"""
<title>darkNet</title>
<a class="links" href="https://pcoding.ru/pdf/algo.pdf" target="_blank">
    algo.pdf
</a>
"""