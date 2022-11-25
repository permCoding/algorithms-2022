def get_tpl(file_name, sep=','):
    with open(file_name) as f:
        lines = f.readlines()
    return [tuple(map(int, line.split(sep))) for line in lines]


def find(x, y, p):
    if x == rx-1 and y == ry-1: print(p)
    else:
        if x+1 < rx: find(x+1, y, p+lab[y][x+1])
        if y+1 < ry: find(x, y+1, p+lab[y+1][x])


lab = get_tpl('./ways/ways4.txt')
rx, ry = len(lab[0]), len(lab)
find(0,0,lab[0][0])
