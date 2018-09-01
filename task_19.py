#task_19

'''
Написать функцию для поиска разницы между максимальным и минимальным числом
среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
'''

import random

def diff_min_max(num_limit, lower_bound, upper_bound):
    num_lower = random.randint(lower_bound,upper_bound)
    num_upper =0
    for i in range(num_limit):
        current_value = random.randint(lower_bound,upper_bound)
        if num_lower >=current_value:
            num_upper=current_value
        if num_upper <=current_value:
            num_upper = current_value
        print(current_value)
    result = num_upper - num_lower
    return result

print('Difference is:',diff_min_max(50, 20, 100))