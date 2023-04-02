import re


with open("./b4-findall.ini", "r", encoding="utf8") as f:
    txt = f.read()

# ptn = r"^дата:\s*([0-2][0-9][.][01][0-9][.][12][0-9]\d\d)"
ptn = r"([0-2][0-9][.][01][0-9][.][12][0-9]\d\d)"

reg = re.compile(ptn, re.M)
res = reg.findall(txt)
for item in res:
    print(item)
