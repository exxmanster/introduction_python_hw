#task_26
'''
Создайте список из 11 случайных целых чисел из отрезка [-1;1]. Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
Однако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None, а не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!
     def calc_frequency(lst): # returns the most frequent number or None
		pass
	Например:
		для [1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0] надо вернуть None
		для [1, 1, 1, 1, -1, 1, 1, -1, 0, 0, 0] надо вернуть 1

'''

import random


lst = [random.randint(-1, 1) for i in range(11)]

print(lst)


def calc_frequency(lst): # returns the most frequent number or None
    one = 0
    _one = 0
    null = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            one += 1
        elif lst[i] == -1:
            _one += 1
        else:
            null += 1
    max_count = one
    max_value = 1
    if _one > max_count:
        max_count = _one
        max_value = -1
    if null > max_count:
        max_count = null
        max_value = 0
    if (one == _one) or (one == null) or (_one == null):
        return None
    else:
        return max_value

print(calc_frequency(lst))