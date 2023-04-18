import findMaxFunc as biggest
from packages import filesFunc
from packages import currentDate

filename = str(input("Enter filename: "))
f = filesFunc.fileFunc(filename)
print(f)
currentDate.dateTime()
