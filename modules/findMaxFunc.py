def biggest(a):
    max = a[0]
    for item in a[1:]:
        if item > max:
            max = item
    print("Наибольшее число: ", max)

