#task_15

'''
Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом.
def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
			pass

'''

import math

def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    if d > math.fabs(r1 + r2) or d < math.fabs(r1 - r2):
        return False
    else:
        return True

print(circles_intersect(10, 5, 5, 6, 7, 2))

