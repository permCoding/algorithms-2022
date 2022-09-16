import timeit 
import algo_sort as m


max_count = 10000
lst = m.get_lst(max_count)

for count in range(1000, max_count+1, 1000):
    
    lst1 = lst[:count+1]
    lst2 = lst[:count+1]

    start_time = timeit.default_timer() 
    m.sort_bubble(lst1)
    res1 = timeit.default_timer() - start_time
    
    start_time = timeit.default_timer() 
    m.sort_bubble_plus(lst2)
    res2 = timeit.default_timer() - start_time
    
    print(f"{count}\t{round(res1, 2)}\t{round(res2, 2)}")
