import re


def a():
    line = "<br><hr>"
    ptn = r"<(?P<tagA>[a-z]+)><(?P<tagB>[a-z]+)>"
    reg = re.compile(ptn, re.I)
    line = reg.sub(r"<\2><\1>", line)
    print(line)


def b():
    line = "<br><hr>"
    ptn = r"<(?P<tagA>[a-z]+)><(?P<tagB>[a-z]+)>"
    reg = re.compile(ptn, re.I)
    line = reg.sub(r"<\g<2>><\g<1>>", line)
    print(line)


def c():
    line = "<br><hr>"
    ptn = r"<(?P<tagA>[a-z]+)><(?P<tagB>[a-z]+)>"
    reg = re.compile(ptn, re.I)
    line = reg.sub(r"<\g<tagB>><\g<tagA>>", line)
    print(line)


a()
b()
c()
