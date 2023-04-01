import sqlite3  # https://pythonru.com/osnovy/sqlite-v-python
import json


con = sqlite3.connect('./prods.db')
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

with open('prods.json', 'r', encoding='utf8') as f:
    _json = json.load(f)

lst = [(obj['title'],obj['href'],obj['price'],obj['stores']) for obj in _json]

sql_insert = "INSERT INTO prods VALUES(?, ?, ?, ?);"
cur.executemany(sql_insert, lst)
con.commit()

con.close()
