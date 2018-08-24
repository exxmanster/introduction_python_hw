#task_12

'''
Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли,
без использования операторов цикла. a) cо строками, б) без использования строк.

'''

def sum_str(number_value):
    sum_value = int(number_value[0]) + int(number_value[1]) + int(number_value[2])
    return sum_value

def sum_int(number_value):
    number_value = int(number_value)
    a = number_value//100
    b = (number_value - a*100)//10
    c = (number_value - a*100 - b*10)
    sum_value = a + b + c
    return sum_value

number_value = input('Enter a 3 digits number: ')
if len(number_value) == 3:
    calculation_way = input('Select calculation method, 1 - for a string, 2 - for a integer: ')
    if calculation_way in ('1', '2'):
        if calculation_way == 1:
            sum_value = sum_str(number_value)
        else:
            sum_value = sum_int(number_value)
        print('The sum of three digits is', sum_value)
    else:
        print('Error: Wrong selection!!!')
else:
    print('Error: Length of entered number does not equal to 3 digits')