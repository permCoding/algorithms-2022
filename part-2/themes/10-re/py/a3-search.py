import re


lines = [
    "дата: 29,12.2022",
    "дата: 19.08.2023",
    "дата: 55.55.5555",
    "дата: 05.05.regular expressions"
]

for line in lines:
    ptns = [
        r"\d{2}\.\d{2}\.\d{4}",
        r"[0-3][0-9][.][01][0-9][.](19|20)\d\d",
        
    ]
    reg = re.compile(ptns[1])
    res = reg.search(line)

    if res:
        print(res.start(), line)
