#task_28

'''
Создать программу, которая запрашивает у пользователя произвольную строку символов.
Далее программа ее шифрует и выводит на экран в зашифрованном виде. Шифрование происходит путем замены каждого символа символом,
который находится на 5 позиций правее в предопределенной таблице шифрования.
Таблица шифрования задается программистом в виде одномерного списка символов латинского алфавита от a до z и цифр от 0 до 9.
Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
Отсутствующие в таблице шифрования символы, записываются в результирующую строку без изменений. Регистр игнорируется.
Таблица шифрования (a, b, c, d, ..., x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
Например: Исходная строка, которую ввел пользователь: 'secret', 'office 365'
Зашифрованная строка, которую выдала программа: 'xjhwjy', 'tkknhj 8ba'
Примечание: т.н. таблица шифрования может быть представлена как строка или список.
'''

import re
#import string

str_to_encode = "Answer to the Ultimate Question of Life, the Universe, and Everything is.........42"

def encode(str_to_encode): # returns enсoded string
   encryption_table = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
   encryption_table = re.sub(' ', '', encryption_table)
   encryption_table_lst = encryption_table.split(',')
   str_decoded = ''
   #print(encryption_table_lst)
   n = len(encryption_table_lst)
   for char in str_to_encode:
       if char not in encryption_table_lst:
           str_decoded += char
       else:
           for i in range(n):
               if char == encryption_table_lst[i]:
                   new_idx = (i + 5) % n
                   str_decoded += encryption_table_lst[new_idx]
   return str_decoded

print(encode(str_to_encode))