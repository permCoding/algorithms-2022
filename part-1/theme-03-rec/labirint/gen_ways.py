from random import randint as r


rx, ry = 10, 10
rm = 9
lst = []
for y in range(ry):
    row = [str(r(0, rm)) for _ in range(rx)]
    lst.append(row)

lines = [','.join(row)+'\n' for row in lst]

with open(f'./ways{rx}.txt','w') as f:
    f.writelines(lines)
