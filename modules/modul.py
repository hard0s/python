from packages import filesFunc 
from packages import datetime_1 
from packages import celend
# file functions
filename = str(input("Enter filename: "))
f = filesFunc.fileFunc(filename)
print(f)
# datetime functions
datetime_1.currTime()
# celendar function
celend.cel()
