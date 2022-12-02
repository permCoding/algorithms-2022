def get_all_bin(lst):
    combs = []
    n = len(lst)
    for i in range(1 << n):  # combo = 9 -> 1001
        combo = []
        for pos in range(n):
            mask = 1 << pos
            if bool(i & mask):
                combo += [lst[pos]]
        combs += [combo]
    return combs


lst = ['a', 'b', 'c', 'd']
for combo in get_all_bin(lst):
    print(combo)

# 1001 == ['a', 'd']
# 0000
# 1111

'''
<< >>
^
&
|
~

x = 6  # 0110
y = 3  # 0011
print(x & y)  # 2
print(x ^ y)  # 5
print(x | y)  # 7
print(y >> 1)  # 1
print(x << 3)  # 011000

'''