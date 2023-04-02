import re


def a(line):  # ['item2', 'item4']
    ptn = r"\s-([a-z0-9]+)\s"
    print(re.findall(ptn, line, re.I))


def b(line):  # ['item1', 'item3']
    ptn = r"(?:^|\s)-([a-z0-9]+)\s"
    print(re.findall(ptn, line, re.I))


def c(line):  # ['item1', 'item3', 'item5']
    ptn = r"(?:^|\s)-([a-z0-9]+)(?:\s|$)"
    print(re.findall(ptn, line, re.I))


def d(line):  # ['item1', 'item2', 'item3', 'item4', 'item5']
    ptn = r"(?:^|\s)-([a-z0-9]+)(?=\s|$)"
    print(re.findall(ptn, line, re.I))


def e(line):  # ['item1', 'item2', 'item3', 'item4', 'item5']
    ptn = r"-([a-z0-9]+)(?=\s|$)"
    print(re.findall(ptn, line, re.I))


def f(line):  # ['item1', 'item2', 'item3', 'item4', 'item5']
    ptn = r"-([^\s]+)"
    print(re.findall(ptn, line, re.I))


line = "-item1 -item2 -item3 -item4 -item5"
a(line)
b(line)
c(line)
d(line)
e(line)
f(line)
