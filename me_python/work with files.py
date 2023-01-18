file = open('print.txt','a+')


def value(items):
    for item in items:
        print(item, file=file)
    file.close()  # закройте файл после работы с ним.

value([1,2,3,4,5,6,7,8,9,10])
