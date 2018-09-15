#test_5


def nearest_number(number_1, number_2):

    numbers = [number_1, number_2]
    numbers.sort(key=lambda elem: abs(10 - elem))
    return numbers[0]


number_1 = int(input('Enter first number:'))
number_2 = int(input('Enter second number:'))


print(nearest_number(number_1, number_2))