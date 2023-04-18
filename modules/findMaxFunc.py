def biggest(a):
    max = a[0]
    for item in a[1:]:
        if item > max:
            max = item
    print("Наибольшее число: ", max)

# a = list(map(int,input("Введите набор чисел: ").split()))

# b = biggest(a)

# str(b)

# print("Наибольшее число:" + b)
