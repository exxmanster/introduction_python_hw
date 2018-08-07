#Task_2

####Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2


import math


a = 4
b = 8
result = (pow(a, 2) + pow(b, 2))%2

print('TheResult of (a**2 + b**2)%2', 'for a = %.2f and b = %.2f is equel to %d' %(a, b,result))
