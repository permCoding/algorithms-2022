import re
import requests
import json


with open('headers.json') as f:
    headers = json.load(f)

url = "https://pcoding.ru/darkNet.php"
resp = requests.get(url, headers=headers)
resp.encoding = "utf8"
html = resp.text

ptn = r"class=\"links\"\s+href=\"([^\"]+pdf)\""

reg = re.compile(ptn, re.M)
links = reg.findall(html)
links = [link for link in links if link.startswith("https://pcoding.ru/gost/")]

for link in links:
    print(link)
