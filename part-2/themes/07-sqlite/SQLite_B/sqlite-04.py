import sqlite3


def select_all(cur):
    sql_select = """
        SELECT 
            id, 
            CAST(SUBSTR(title, 1, INSTR(title, ' ')-1) as INTEGER) as value, 
            price 
        FROM prods 
        ORDER BY price DESC
    """
    cur.execute(sql_select)
    rows = cur.fetchall()
    return rows


def print_rows(rows):
    for row in rows: 
        print(row)


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
