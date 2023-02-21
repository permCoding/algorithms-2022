from itertools import permutations as p
from itertools import combinations as c

t = list("abcd")
# print(t)

# for e in p(t): print(e)

def get(t):
    w = []
    for k in range(len(t)+1):
        for e in c(t, k):
            w.append(e)
    return w

for q in get(t):
    print(q)
