import random as r

count = 10000
lst = [r.randint(0, count) for _ in range(count)]

lst = list(range(count))
print(lst[:10])

r.shuffle(lst)
print(lst[:10])

s = "Python"
lst = list(s)
r.shuffle(lst)
print(''.join(lst))

print(''.join(r.sample(s, len(s))))
