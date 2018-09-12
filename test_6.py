
def is_isogram(string):
    if isinstance(string, str) and len(string) != 0:
        string = string.lower()
        if len(string) == len(set(string)):
            result = True
        else:
            result = False
    elif not string:
      result = False
    else:
        raise TypeError('Argument should be a string! ')

    return string, result

text= input('Enter A Word: ')
print (is_isogram(text))
