import sqlite3


def select_all(cur):
    sql_select = "SELECT * FROM prods ORDER BY price DESC"
    cur.execute(sql_select)
    rows = cur.fetchall()
    return rows


def print_rows(rows):
    for row in rows: 
        print(row[0], row[1].split()[0], row[3])


def main():
    try:
        con = sqlite3.connect('prods.db')
        cur = con.cursor()

        rows = select_all(cur)
        print_rows(rows)
    except sqlite3.Error as err:
        print(err)
    finally:
        if con:
            con.close()


main()
