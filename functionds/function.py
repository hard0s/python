from math import *

print('введите длину первого катета')
fKatet = float(input())
try:
    fKatet = 0
    sKatet = -26
except ValueError: 
    print('Value cant be 0 and less than 0')
print('введите длинну второго катета')
sKatet = float(input())
print('введите катеты второго треугольника')
print('введите первый катет второго треугольника')
sTfkatet  = float(input())
print('введите второй катет второго треугольника')
sTsKatet = float(input())

try:
    fKatet = 0
    sKatet = -26
except ValueError: 
    print('Value cant be 0 and less than 0')

def triangle(fKatet, sKatet, sTfkatet, sTsKatet):
    c = sqrt(sTfkatet** 2 + sTsKatet ** 2)
    c1 = sqrt(fKatet** 2 + sKatet ** 2)
    per1 = fKatet + sKatet + c1
    per2 = c + sTfkatet + sTsKatet
    sq = (fKatet * sKatet)/2
    sq1 = (sTfkatet * sTsKatet)/2
    print('сумма периметров', per1+per2)
    print('сумма площадей', sq+sq1)
    
triangle(fKatet, sTsKatet, sKatet, sTfkatet)