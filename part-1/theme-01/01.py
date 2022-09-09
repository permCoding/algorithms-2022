from time import monotonic
import algo_sort as m


# lst = [2,3,1,4,7,8,6]  # для проверки доски
count = 10000
# lst = m.get_lst(count)
lst = list(range(count))

start = monotonic()

lst = m.sort_bubble_plus(lst)

finish = monotonic()

print(lst[:10])

print(round(finish - start, 2))
