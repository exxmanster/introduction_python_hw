
#task_11
'''
Написать функцию, которая будет переводить градусы в радианы (без использования math.radians). Используя эту функцию,
вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
def degrees2radians(degrees): # returns float
            pass

'''

import math

def degrees2radians(degrees): # returns float

    #pi = 22 / 7
    radian = degrees * (math.pi / 180)

    return radian


print('Value in Radians for 60 degrees is %.2f' %degrees2radians(40))
print('Value in Radians for 45 degrees is %.2f' %degrees2radians(45))
print('Value in Radians for 40 degrees is %.2f' %degrees2radians(60))