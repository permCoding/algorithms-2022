import re


lines = [
    "price 100$",
    "price 5200$",
    "цена 128000 руб.",
    "стоимость - 20 руб.",
    "time 12:34:56",
    "data 2023/02/12",
    "regular expressions"
]

for line in lines:
    ptns = [
        r"\d{2,}",
        r"[0-9]{4}",
        r"[0-9]{4}\D+",
        r"\D+[0-9]{4}\D+",
    ]
    reg = re.compile(ptns[3])
    res = reg.search(line)

    if res:
        print(res.start(), line)
