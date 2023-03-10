import requests


def get_html(url):
    ua = { 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" 
    }
    ob = requests.get(url, headers=ua)
    ob.encoding = 'utf8'
    return ob.text


def get_links():
    lst = []
    a, b = '<a class="links" href="', '" target=_blank>'
    pos = 0
    while html.find(a, pos) > -1:
        posa = html.find(a, pos) + len(a)
        posb = html.find(b, posa)
        lst.append(html[posa:posb])
        pos = posb
    return lst


url = "https://pcoding.ru/darkNet.php"

html = get_html(url)
a, b = '<title>', '</title>'
posa = html.find(a) + len(a)
posb = html.find(b)
print(html[posa: posb])

links = map(lambda e: e+'\n' , get_links())
with open('links.txt', 'w', encoding='utf8') as f:
    f.writelines(links)

"""
<title>darkNet</title>
<a class="links" href="https://pcoding.ru/pdf/AgroRobot.pdf" target=_blank>
        AgroRobot.pdf
</a>
<a class="links" href="https://pcoding.ru/gost/opisProg.doc" target="_blank">
    opisProg.doc
</a>
"""