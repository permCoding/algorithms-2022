import requests


def get_html(url):
    ua = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" 
    }
    ob = requests.get(url, headers=ua)
    ob.encoding = 'utf8'
    return ob.text


def get_data():
    lst = []    
    pos = 0
    a = '<div class="product-title__head">'
    while html.find(a, pos) > -1:
        a, b = '<div class="product-title__head">', '</div>'
        posa = html.find(a, pos) + len(a)
        posb = html.find(b, posa)
        name = html[posa:posb].strip() \
            .replace('&quot;','"') \
            .replace('&nbsp;','"')

        a, b = '<div class="product-title__author">', '</div>'
        posa = html.find(a, pos) + len(a)
        posb = html.find(b, posa)
        author = html[posa:posb].strip() \
            .replace('&quot;','"') \
            .replace('&nbsp;','"')
        
        lst.append((name,author))
        pos = posb
    return lst


url = "https://www.chitai-gorod.ru/catalog/books/fantastika-fentezi-9692?page=1"
html = get_html(url)
res = get_data()
for e in res: print(e)

# links = map(lambda e: e+'\n' , get_links())
# with open('links.txt', 'w', encoding='utf8') as f:
#     f.writelines(links)

"""

ДОРАБ ПАДЖИНАЦИЮ



<div class="product-title">
    <div class="product-title__head">
        Заложники солнца
    </div> 
    <div class="product-title__author">
        Мила Бачурова
    </div>
</div>
"""