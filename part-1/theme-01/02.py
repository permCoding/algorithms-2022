import random as r

lst = list(range(10))

print(lst)

r.shuffle(lst)

print(lst)

s = "Python"
lst = list(s)
r.shuffle(lst)
print(''.join(lst))

print(''.join(r.sample(s, len(s))))
