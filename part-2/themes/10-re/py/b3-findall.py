import re


txt = """\n
дата: 29,12.2022",\n
дата: 19.08.2023",\n
дата: 05.05.2005 год",\n
дата:25.01.2021",\n
дата: 55.55.5555",\n
дата: 05.05.expressions"\n
date: 19.02.2020",\n
date: 109.02.2020",\n
"""

ptns = [
    r"^дата:\s*([0-2][0-9][.][01][0-9][.][12][0-9]\d\d)",
    
]
reg = re.compile(ptns[0], re.M)
res = reg.findall(txt)
for item in res:
    print(item)
