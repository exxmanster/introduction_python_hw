# Task_5

### Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )

import math

a = 1024
b = 128
c = 512
result = math.fabs(a - b) / math.pow(( a + b),3) - math.cos(c)

print ('The result of | a - b | /( a + b)3 - cos( c ) with a = %d b = %d c = %d is equal to %f' % (a,b,c,result) )