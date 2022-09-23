# 1 1 2 3 5 8 13 21 34 55

from unittest import result


def fib(n):
    if n < 3: return 1
    return fib(n-1) + fib(n-2)


def fib_cash(n):
    if n < 3: return 1
    if lst[n-1] == 0: lst[n-1] = fib_cash(n-1)
    if lst[n-2] == 0: lst[n-2] = fib_cash(n-2)
    return lst[n-1] + lst[n-2]


def fib_for(n):
    if n < 3: return 1
    a, b = 1, 1
    '1 1 2 3 5 8 13'
    for _ in range(2, n):
        a, b = b, a + b
    return b


n_fib = 55
lst = [0] * (n_fib+1)
print(fib_cash(n_fib))
print(fib_for(n_fib))
