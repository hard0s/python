def biggest(mx, *args):
    for a in args:
        if mx < a: mx = a
    return mx

a = list(map(int,input("Введите набор чисел: ").split()))

b = biggest(a)

str(b)

print("Наибольшее число:" + b)
