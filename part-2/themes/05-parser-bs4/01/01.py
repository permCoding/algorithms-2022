import requests


def get_html(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    resp = requests.get(url, headers=head)
    resp.encoding = "utf8"
    return resp.text


url = "https://www.championat.com/hockey/_superleague/tournament/5077/table/#all"
html = get_html(url)
with open("tournament.html", 'w', encoding='utf8') as f:
    f.write(html)
