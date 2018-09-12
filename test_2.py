def main(a, b, c):
    if c == 0:
        return 'Error: division by zero'
    else:
        return a - 4*b/c
print(main(2, 3, 0))