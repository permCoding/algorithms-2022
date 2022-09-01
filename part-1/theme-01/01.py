from random import shuffle, sample


# lst = list(range(0,9))
# shuffle(lst)
# print(lst)


# lst = list('абракадабра')
# shuffle(lst)
# print(''.join(lst))


s = 'абракадабра'
lst = sample(s, len(s))
print(''.join(lst))