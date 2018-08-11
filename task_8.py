
#Task_8

#Дана строка с именем студента, в которой имя предшествует фамилии,
#  например  ‘Mark Zuckerberg‘. Написать программу, которая преобразует эту строку, ставя фамилию на первое место,
#  а имя на второе. Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.


fullname = 'Jeff Bezos'
first_name = fullname.split(' ')[0]
last_name = fullname.split(' ')[1]
print('Reverse name for the',fullname,'is',last_name, first_name)