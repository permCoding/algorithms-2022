import sys


def fact(n):
    if n == 1: return 1
    return fact(n-1) * n


def f1():
    return 1


def f2():
    return 2


# amount = 0
# for _ in range(10000):
#     amount += f1() + f2()
# print(amount)

sys.setrecursionlimit(20000)

print(len(str(fact(2000))))
