#Task_4

###Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c

a = 25
b = -25
c = 18
if a + b != 0:

    result = (a - b *c) / (a + b) % c
    print('The result of (a - b * c ) / ( a + b ) %',' c  a = %d for b = %d  c = %d is equal to = %f' %(a, b, c, result))
else:
    print('Error: Division by ZERO!!!')