import sqlite3
import json


def create_table(cur):
    sql_create = """
    CREATE TABLE IF NOT EXISTS prods(
        id INTEGER UNIQUE,
        title TEXT,
        href TEXT,
        price INTEGER,
        stores TEXT,
        PRIMARY KEY (id AUTOINCREMENT)
    );
    """
    cur.execute(sql_create)
    con.commit()


def get_objects(filename):
    with open(filename, 'r', encoding='utf8') as f:
        _json = json.load(f)
    for obj in _json:
        obj['price'] = int(obj['price'].replace(' ', '').replace('₽', ''))
    lst = [(obj['title'],obj['href'],obj['price'],obj['stores']) for obj in _json]
    return lst


def insert_records(cur, lst):
    sql_insert = """
        INSERT INTO prods ('title','href','price','stores') 
        VALUES(?, ?, ?, ?);
    """
    cur.executemany(sql_insert, lst)
    con.commit()    


def select_all(cur):
    sql_select = "SELECT * FROM prods"
    cur.execute(sql_select)
    rows = cur.fetchall()
    return rows


con = sqlite3.connect('prods.db')
cur = con.cursor()

create_table(cur)
lst = get_objects('prods.json')
insert_records(cur, lst)
rows = select_all(cur)
for row in rows: print(row)

con.close()
