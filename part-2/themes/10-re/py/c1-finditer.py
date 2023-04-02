import re


def ex_a(line, ptn):
    reg = re.compile(ptn, re.U)  # UNICODE
    res = reg.search(line)
    print(res)
    if res:  # Match | None
        print(res[0], res.span(), \
            res.span()[0], res.span()[1], \
            res.start(), res.end())


def ex_b(line, ptn):
    reg = re.compile(ptn, re.U)
    print(reg.findall(line))


def ex_c(line, ptn):
    reg = re.compile(ptn, re.U)
    iter = re.finditer(reg, line)
    for m in iter:
        print(m, "-->", m[0])  # Match
    # print([m.span() for m in iter])  # итератор исчерпывается
    print([m.span() for m in re.finditer(reg, line)])


line = "aabaabaaab"
# ex_a(line, r"ab")
# ex_b(line, r"ab")
ex_c(line, r"ab")
