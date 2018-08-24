#task_16
'''
Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.
def have_trains_crashed(v1, v2): # returns boolean value
			pass

'''

def have_trains_crashed(v1, v2): # returns boolean value
    d = 10
    s1 = 4
    t1 = s1/v1
    s2 = v2*t1
    if s2 < (d - s1):
        return ("Trains will not crash! ") #False
    else:
        return ("Trains will crash! ") #True

print(have_trains_crashed(5,9))