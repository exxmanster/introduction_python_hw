#task_17
'''
Написать функцию решения квадратного уравнения.
		def solve_quadratic_equation(a, b, c): # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
			pass

'''

import math
import cmath

def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots, 1 root and None or 2 Nones
    d=math.pow(b,2)-4*a*c
    if d > 0:
        return (-b+math.sqrt(d))/2/a, (-b-math.sqrt(d))/2/a
    else:
        if d == 0:
            return -b/2/a, None
        else:
            return None, None

print(solve_quadratic_equation(44, 87, 13))