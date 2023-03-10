def get_tab(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        tab = [[int(n) for n in s.split(',')] for s in lines]
    return tab


def find_way_rec(x, y, v):
    if x == rx-1 and y == ry-1: ways.append(v)
    if x < rx-1: find_way_rec(x+1, y, v+t[y][x+1])
    if y < ry-1: find_way_rec(x, y+1, v+t[y+1][x])
    

t = get_tab('./ways/ways3.txt')
for row in t: print(*row)
rx, ry = len(t[0]), len(t)

ways = []
find_way_rec(0,0,t[0][0])
print(ways)  # ценности всех путей
print(len(ways))  # кол-во путей
print(f'len max way = {max(ways)}')
