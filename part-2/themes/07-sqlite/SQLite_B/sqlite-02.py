import sqlite3


def select_all(cur):
    sql_select = "SELECT * FROM prods ORDER BY price DESC"
    cur.execute(sql_select)
    rows = cur.fetchall()
    return rows


con = sqlite3.connect('prods.db')
cur = con.cursor()

rows = select_all(cur)
for row in rows: print(row[0], row[1].split()[0], row[3])

con.close()
