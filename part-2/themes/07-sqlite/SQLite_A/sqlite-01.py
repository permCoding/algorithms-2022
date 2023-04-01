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

con.close()
