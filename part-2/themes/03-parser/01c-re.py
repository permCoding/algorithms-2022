import requests
import re


def get_html(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    resp = requests.get(url, headers=head)
    resp.encoding = "utf8"
    return resp.text


url = 'https://pcoding.ru/darkNet.php'
html = get_html(url)

ptn = "<title>(.*)</title>"
res = re.search(ptn, html, re.I)
print('title -', res.group(1))

ptn = r"<a\s+class=\"links\"\s+href=\"([^\"]+\.pdf)\"[^\"]+>([^<]+)"

links = re.findall(ptn, html, re.I)
for link in links:
    print(link[1], '-', link[0])
    break

"""
<title>darkNet</title>
<a class="links" href="https://pcoding.ru/pdf/algo.pdf" target="_blank">
    algo.pdf
</a>
"""