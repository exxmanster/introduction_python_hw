def main(a, b, c):
    if c == 1:
        return 'Error: division by Zero!'
    else:
        return (a*b + 4)/(c - 1)
print(main(2, 3, 1))