from time import monotonic
from os import system


system("cls")

words = open("./words.csv", mode="r", encoding="windows-1251").read().split('\n')
print(words[-9:-1])  # для контроля

find_words = [
    "як", "абак", "кукуруза", "ящик", 
    "ящик",  "ящик", "оса", "орёл", "орел"
]

n = len(find_words)
results = [-1] * n

for pos in range(n):
    fw = find_words[pos]
    a = monotonic()
    for word in words:
        if word == fw:
            b = monotonic()
            results[pos] = round(b-a, 4)
            break

lst = sorted(zip(results, find_words), key=lambda x: x[0])
for item in lst:
    print(f"{item[0]}\t{item[1]}")
