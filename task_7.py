#Task_7

# Преобразовать строку с американским форматом даты в европейский.Например,'05.17.2016' преобразуется в '17.05.2016'



#strings method
date = '09.08.2018'
date_lst = date.split('.')
date_eu = date_lst[1] + '.' + date_lst[0] + '.' + date_lst[2]
print('European format for %s is %s' %(date, date_eu))

#datetime method

import datetime


format_str = '%m.%d.%Y'
datetime_obj = datetime.datetime.strptime(date, format_str)
date_eu_2 = datetime.datetime.strftime(datetime_obj,'%d.%m.%Y')
print('European format for %s is %s' %(date, date_eu_2))