from functools import reduce
import sys


def fact(n):
    return reduce(lambda acc, tmp: acc * tmp, range(1, n), 1)

    # result = 1
    # for i in range(1, n):
    #     result *= i
    # return result
    
    # if n == 1: return 1
    # return fact(n-1) * n


def f1():
    return 1


def f2():
    return 2


# amount = 0
# for _ in range(10000):
#     amount += f1() + f2()
# print(amount)

sys.setrecursionlimit(20000)

print(len(str(fact(20000))))
