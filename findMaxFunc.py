def biggest(* args):
    max = args[0]
    for item in args[1:]:
        if item > max:
            max = item
    return max

a = list(map(int,input("Введите числа в массив: ").split(' ')))

b = biggest(a)

str(b)

print(b)
