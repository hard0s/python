import datetime
from calendar import Calendar
import calendar

#Раздельный показ произвольной даты
d = datetime.date(2012, 12, 21)
print(d.year)
print(d.day) 
print(d.month) 

#Сегодняшняя дата
print(datetime.date.today())

#Раздельный и совместный вывод даты и времени
b = datetime.datetime(2012, 12, 21, 12, 30, 10)
print(b) # datetime.datetime(2012, 12, 21, 12, 30, 10)
 
d = datetime.datetime(2012, 12, 21, 12, 30, 10)
print(d.year)
print(d.second)
print(d.hour)

#Вывод даты в заданном формате
today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '31/01/2023'

print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # '2031-01-23-текущее время'

c = Calendar()
#c.monthdatescalendar(2023, 12)
print(c.yeardatescalendar(2023, 1))
print(calendar.prmonth(2023, 12))
import calendar
calendar.prcal(2023)


