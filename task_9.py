#Task_9

#Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase. Для простоты считаем,
#  что имя переменной всегда состоит из 3-х слов. Например: 'employee_first_name' -> 'EmployeeFirstName'


snake_style = 'employee_first_name'
var_str = snake_style.split('_')
CamelCase = var_str[0].title() + var_str[1].title() + var_str[2].title()
print('CamelCase for %s is %s' %(snake_style, CamelCase))