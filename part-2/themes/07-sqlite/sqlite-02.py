import sqlite3


con = sqlite3.connect('prods.db')
cur = con.cursor()

sql_create = """
CREATE TABLE IF NOT EXISTS prods(
    title TEXT,
    href TEXT,
    price TEXT,
    stores TEXT
);
"""
cur.execute(sql_create)
con.commit()

_json = \
    [
        {
            "title": "120 ГБ 2.5\" SATA накопитель Team Group GX1 [T253X1120G0C101] [SATA, чтение - 500 Мбайт/сек, запись - 320 Мбайт/сек, 2D NAND 3 бит TLC]",
            "href": "https://www.dns-shop.ru/product/2046fc61ba4a3332/120-gb-25-sata-nakopitel-team-group-gx1-t253x1120g0c101/",
            "price": "950 ₽",
            "stores": "В наличии: в 18 магазинах"
        },
        {
            "title": "128 ГБ 2.5\" SATA накопитель Tammuz GK300 [TGK30128A58] [SATA, чтение - 500 Мбайт/сек, запись - 400 Мбайт/сек, 3D NAND 3 бит TLC]",
            "href": "https://www.dns-shop.ru/product/bdf0436e70ca3332/128-gb-25-sata-nakopitel-tammuz-gk300-tgk30128a58/",
            "price": "950 ₽",
            "stores": "В наличии: в 4 магазинах"
        },
        {
            "title": "120 ГБ 2.5\" SATA накопитель Hikvision C100 [HS-SSD-C100/120G] [SATA, чтение - 550 Мбайт/сек, запись - 420 Мбайт/сек, 3D NAND 3 бит TLC]",
            "href": "https://www.dns-shop.ru/product/14c2dcc11fab3332/120-gb-25-sata-nakopitel-hikvision-c100-hs-ssd-c100120g/",
            "price": "999 ₽",
            "stores": "В наличии: в 1 магазине"
        }
    ]
lst = [(obj['title'],obj['href'],obj['price'],obj['stores']) for obj in _json]

sql_insert = "INSERT INTO prods VALUES(?, ?, ?, ?);"
cur.executemany(sql_insert, lst)
con.commit()

con.close()
