#Task_6

###Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a |

import math

a = 5
b = 10
c = 7

if b != 0:
    abc_result = math.pow(math.log1p(1 + c)/(-b), 4) + math.fabs(a)
    print('The result of (ln(1 + c) / -b)4 + |a| for a = %d, b = %d, c = %d is equal to %.10f'
    %(a, b, c, abc_result))
else: print('Error: division by ZERO!!!')