import random

lst =[9,6,5,3,7,8,2,3,1,0]

def swap_min_max(lst):
    max= lst[0]
    min= lst[0]
    max_idx= 0
    min_idx = 0
    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
            max_idx = i
        if min > lst[i]:
            min = lst[i]
            min_idx = i
    lst[max_idx] = min
    lst[min_idx] = max
    return lst

print(swap_min_max(lst))