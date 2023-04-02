import re


def repl(m):
    return f"    {m.group(1)}: {m.group(2)}"


with open("./g3-replace.ini", "r", encoding="utf8") as f:
    ini = f.read()

ptn = r"^\s*(\"[-a-z0-9]+\")\s*:\s*(\"?[-a-z0-9]+\"?)\s*,*\s*$"

reg = re.compile(ptn, re.M | re.I)

for r in reg.findall(ini): print(r)  # для контроля

ini = reg.sub(lambda m: f"    {m.group(1)}: {m.group(2)}", ini)
print(ini)  # для контроля

with open("./repl+.ini", "w", encoding="utf8") as f:
    f.write(ini)
