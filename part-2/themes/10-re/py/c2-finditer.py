import re
import requests
import json


def get_html(url):
    with open('headers.json') as f:
        headers = json.load(f)
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf8"
    return resp.text


def get_links_pdf(html):
    ptn = r"(class=\"links\"\shref=\")([^\"]+\.pdf)(\")"
    reg = re.compile(ptn)
    # iter = re.finditer(reg, html)  # ver.1
    iter = reg.finditer(html)  # ver.2
    return [link[2] for link in iter]  # берём группу по индексу, 0 - full


def get_links_pdf_a(html):
    ptn = r"(class=\"links\"\shref=\")([^\"]+\.pdf)(\")"
    reg = re.compile(ptn)
    iter = reg.finditer(html)  # ver.2
    return [link.group(2) for link in iter]  # берём группу по индексу, 0 - full


def get_links_pdf_b(html):
    ptn = r"(?<=class=\"links\"\shref=\")([^\"]+\.pdf)(?=\")"
    reg = re.compile(ptn)
    iter = reg.finditer(html)  # ver.2
    return [link.group(0) for link in iter]  # берём группу по индексу, 0 - full


def get_links_pdf_c(html):
    ptn = r"(?<=class=\"links\"\shref=\")(?P<link>[^\"]+\.pdf)(?=\")"
    reg = re.compile(ptn)
    iter = reg.finditer(html)
    return [link.group("link") for link in iter]  # берём группу по индексу, 0 - full


def get_links_filtred(links, ftr):
    ptn = ".+/" + ftr + r"/.+"  # .../gost/...
    reg = re.compile(ptn, re.I)
    lst = []
    for link in links:
        res = reg.search(link)
        if res:  # можно брать срезами по строке
            lst.append(link[res.start():res.end()])
    return lst


def get_links_filtred_a(links, ftr):
    ptn = f"/{ftr}/"  # когда не нужны сложные проверки
    return [link for link in links if ptn in link]


url = "https://pcoding.ru/darkNet.php"
html = get_html(url)

links = get_links_pdf(html)
# links = get_links_pdf_a(html)
# links = get_links_pdf_b(html)
# links = get_links_pdf_c(html)

# for link in links: print(link)

filtred = get_links_filtred(links, "gost")  # назначаем фильтр по каталогу

# filtred = get_links_filtred_a(links, "pdf")  # назначаем фильтр по каталогу

for link in filtred: print(link)
