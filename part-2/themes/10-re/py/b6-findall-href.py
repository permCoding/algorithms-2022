import re
import requests


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf8"
    return resp.text


html = get_html(url = "https://pcoding.ru/darkNet.php")

ptn = r"class=\"links\"\s+href=\"([^\"]+pdf)\""
reg = re.compile(ptn, re.M)

results = reg.findall(html)
for item in results: print(item)

"""
<a class="links" href="https://pcoding.ru/pdf/algo.pdf" target="_blank">
    algo.pdf
</a>
"""