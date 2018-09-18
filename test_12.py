import random


def x_y():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    return [x, y, x * y]


def table_z():
    already = []
    for i in range(15):
        z = x_y()
        while 1:
            if z in already or [z[1], z[0], z[2]] in already:
                z = x_y()
            else:
                print('%s) %s * %s = %s' % (i + 1, z[0], z[1], z[2]))
                already.append(z)
                break


table_z()