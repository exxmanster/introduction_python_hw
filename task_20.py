#task_20
'''
Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit
случайно сгенерированных чисел в указанном числовом диапазоне.
Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
		     pass
'''


import random

def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
    gen_number = 0
    total = 0
    even_sum = 0
    odd_sum = 0

    for i in range(num_limit):
        gen_number=random.randint(lower_bound,upper_bound)

        # if i % num_limit:
        #     continue
        if gen_number % 2 == 0:
            even_sum += gen_number

        else:
            odd_sum += gen_number

    total=even_sum-odd_sum
    return total

print(diff_even_odd(500,100,1000))