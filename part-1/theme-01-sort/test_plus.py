from timeit import default_timer as t
from random import randint as r
import sort_plus as s
import sys

# sys.setrecursionlimit(30000)
count = 200000
lst = [r(0, 1000000) for _ in range(count)]
print(lst[:10])

start = t()

# res = s.sort_merge(lst)

res = s.sort_quick(lst)

print(round(t() - start, 3))
print(res[:10])
