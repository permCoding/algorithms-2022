def rec(combo, deep):
    if deep == len(lst):  # точка останова
        print(combo)
    else:  # шаги рекурсии
        rec(combo+[lst[deep]], deep+1)
        rec(combo, deep+1)


lst = ['a', 'b', 'c', 'd']
rec([], 0)
