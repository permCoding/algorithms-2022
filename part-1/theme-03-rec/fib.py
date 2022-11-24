# числа Фибоначчи - 1 1 2 3 5 8 13 

def fib(n):
    if n < 3: return 1
    return fib(n-2) + fib(n-1)


def fib_cash(n):
    if n < 3: return 1
    if lst[n-1] == 0:
        lst[n-1] = fib_cash(n-1)
    if lst[n-2] == 0:
        lst[n-2] = fib_cash(n-2)
    return lst[n-2] + lst[n-1]


n = 100
lst = [0,1,1] + [0] * n
print(fib_cash(n))
# print(fib(n))  # тут без кэша нельзя - добавит кэш от Питона
