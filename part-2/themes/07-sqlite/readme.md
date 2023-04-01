# SQLite  

> установить в VS Code расширение SQLite Viewer  
> для просмотра БД и таблиц  

---  

## SQLite docs  

https://www.sqlite.org/datatype3.html  

NULL  
INTEGER  
REAL  
TEXT  
BLOB  

```py
cursor.fetchone()  
cursor.fetchall()  
cursor.fetchmany(size)  

```

```sql
CREATE TABLE "first" (
    "id" INTEGER UNIQUE,
    "title" TEXT,
    "rating" REAL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

---  
