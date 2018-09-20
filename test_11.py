import numpy


matrix = [[3, 8, 7], [5, 9, 6], [2, 6, 7]]

def sort_alt(matrix):
    array = numpy.array(matrix)
    tr = array.transpose()
    for i in range( len(matrix)):
        if (i % 2 == 0):
            tr[i].sort()
        else:
            tr[i] = -tr[i]
            tr[i].sort()
            tr[i] = -tr[i]
    array = tr.transpose()
    return array

print(sort_alt(matrix))