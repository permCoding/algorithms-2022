def get_all_combs(lst):
    def rec(combo, deep):
        if deep == len(lst):  # точка останова
            combs.append(combo)
        else:  # шаги рекурсии
            rec(combo+[lst[deep]], deep+1)
            rec(combo, deep+1)
    combs = []
    rec([], 0)
    return combs


lst = ['a', 'b', 'c', 'd']
combs = get_all_combs(lst)
for combo in sorted(combs, key=lambda x: len(x)):
    print(combo)
