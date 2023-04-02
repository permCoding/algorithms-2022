import re


lines = [
    "12 34 56 78",
    "12 34-56 78",
    "12;34;56 78",
    "12-34-56-78",
    "12.34.56.78",
    "12:34:56:78",
]


ptn = r"[-\.\s]"  # [-\.\s;:]
for line in lines:
    reg = re.compile(ptn, re.I)
    print(line, reg.split(line, 2))  # limit = 2
