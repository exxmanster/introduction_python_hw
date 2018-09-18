#task_7


def fib_10():

    a, b = 1, 1
    num = 10
    result = a + b
    num_int = int(num - 2)

    for i in range(num_int):
        a, b = b, a + b
        result += b
    return result

print(fib_10())