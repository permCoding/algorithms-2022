import re


with open("./g2-replace.ini", "r", encoding="utf8") as f:
    ini = f.read()

ptn = r"^\s*([a-z]+)\s*[-:]\s*(\w+-*\w+)"
reg = re.compile(ptn, re.M)

ini = reg.sub(lambda m: f"{m.group(1)}: {m.group(2)}", ini)

with open("./repl+.ini", "w", encoding="utf8") as f:
    f.write(ini)
