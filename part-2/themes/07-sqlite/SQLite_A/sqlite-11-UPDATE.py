import sqlite3  # https://pythonru.com/osnovy/sqlite-v-python
import json


con = sqlite3.connect('./prods.db')
cur = con.cursor()

sql_update = "UPDATE prods SET price=REPLACE(price, ' ', '');"
cur.execute(sql_update)
sql_update = "UPDATE prods SET price=REPLACE(price, '₽', '');"
cur.execute(sql_update)
con.commit()

sql_select = "SELECT * FROM prods"
cur.execute(sql_select)
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()
