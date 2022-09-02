from time import monotonic
import algo_sort as m


start = monotonic()

m.sort_sleep()

finish = monotonic()

print(finish - start)
