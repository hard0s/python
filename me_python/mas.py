from random import randint
x = []
i = 0
while len(x) != 20:
    i = randint(-20, 20)#числа подбираются случайным образом в диапозоне от 0 до 20
    if i not in x:  #функция используется для исключения возможности повторений
        x.append(i)
print(x)