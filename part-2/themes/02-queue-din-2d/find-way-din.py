def get_tab(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        tab = [[int(n) for n in s.split(',')] for s in lines]
    return tab


def find_way_din():
    tmp = [[0]*rx for _ in range(ry)]
    tmp[0][0] = t[0][0]
    for x in range(1, rx): tmp[0][x] = tmp[0][x-1] + t[0][x]
    for y in range(1, ry): tmp[y][0] = tmp[y-1][0] + t[y][0]
    for y in range(1, ry):
        for x in range(1, rx):
            base = max(tmp[y-1][x], tmp[y][x-1])
            tmp[y][x] = t[y][x] + base
    return tmp


t = get_tab('./ways/ways3.txt')
for row in t: print(*row)
rx, ry = len(t[0]), len(t)

res = find_way_din()
for row in res:
    print(*row)
print(f'len max way = {res[ry-1][rx-1]}')
